import os
import time
import json
import hmac, hashlib
from requests import Request, Session, exceptions
from selenium import webdriver
from urllib3.util import parse_url
import requests

from .product import Product
from .mediaspace import MediaSpace
from .shop import Shop
from .merchant import Merchant
from .order import Order
from .logistics import Logistics
from .firstmile import FirstMile
from .payment import Payment
from .discount import Discount
from .bundledeal import BundleDeal
from .addondeal import AddonDeal
from .voucher import Voucher
from .followprize import FollowPrize
from .toppicks import Toppicks
from .returns import Returns
from .accounthealth import AccountHealth
from .chat import Chat
from .public import Public
from .push import Push

# installed sub-module
registered_module = {
    "product": Product,
    "mediaspace": MediaSpace,
    "shop": Shop,
    "merchant": Merchant,
    "order": Order,
    "logistics": Logistics,
    "firstmile" : FirstMile,
    "payment" : Payment,
    "discount" : Discount,
    "bundledeal": BundleDeal,
    "addondeal": AddonDeal,
    "voucher" : Voucher,
    "followprize" : FollowPrize,
    "toppicks": Toppicks,
    "returns" : Returns,
    "accounthealth" : AccountHealth,
    "chat" : Chat,
    "public" : Public,
    "push" : Push
#    "shopcategory": ShopCategory,
#    "item": Item,
#    "image": Image,
#    "discount": Discount,
#    "order": Order,
#    "logistic": Logistic,
#    "returns": Returns,
#    "rma": RMA,
#    "public": Public,

}


class ClientMeta(type):
    def __new__(mcs, name, bases, dct):
        klass = super(ClientMeta, mcs).__new__(mcs, name, bases, dct)
        setattr(klass, "registered_module", registered_module)
        return klass


class Client(object, metaclass=ClientMeta):
    __metaclass__ = ClientMeta

    ### declare CACHED_MODULE in __init__
    # CACHED_MODULE = {}

    BASE_URL = "https://partner.shopeemobile.com"
    BASE_TEST_URL = "https://partner.test-stable.shopeemobile.com"
    BASE_API_URL = "/api/v2/"

    # PER_MINUTE_API_RATE = 1000

    def __init__(self, shop_id, partner_id, partner_key, redirect_url, test_env=False, code = None ,access_token = None, refresh_token = None):
        ''' initialize basic params and cache class
        '''
        if test_env:
            self.BASE_URL = self.BASE_TEST_URL
        self.partner_id = int(partner_id)
        self.partner_key = partner_key
        self.redirect_url = redirect_url
        self.host = self.BASE_URL
        self.shop_id = int(shop_id)
        self.code = code
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.timeout = None

        self.CACHED_MODULE = {}

    def __getattr__(self, name):
        try:
            value = super(Client, self).__getattribute__(name)
        except AttributeError as e:
            value = self._get_cached_module(name)
            if not value:
                raise e
        return value

    def _make_timestamp(self):
        return int(time.time())

    def set_access_token(self, access_token):
        self.access_token = access_token

#    def set_additional_parameter(self, parameter, timest, access_token, sign):
#        add_param = {
#            "Sign" : sign,
#            "Timestamp" : timest,
#            "access_token" : access_token
#        }
#        parameter.update(add_param)
#        return parameter
    def _make_default_parameter(self, timest, sign):
        return {
            "Partner_id": self.partner_id,
            "Timestamp": timest,
            "Access_token": self.access_token,
            "Shop_id": self.shop_id,
            "Sign": sign
        }

    def _make_short_default_parameter(self, timest, sign):
        return {
            "Partner_id": self.partner_id,
            "Sign": sign,
            "Timestamp": timest
        }

    def _api_sign(self, path, timest):
        base_string = f'{self.partner_id}{path}{timest}{self.access_token}{self.shop_id}'.encode()
        sign = hmac.new(self.partner_key.encode(), base_string, hashlib.sha256).hexdigest()
        return sign

    def _api_short_sign(self, path, timest):
        base_string = f'{self.partner_id}{path}{timest}'.encode()
        sign = hmac.new(self.partner_key.encode(), base_string, hashlib.sha256).hexdigest()
        return sign

    def _api_url(self, path):
        url = self.host + path
        return  url

    def _create_parameter_url(self, url, parameter):
        if parameter !=None:
            url = url + "?"
            par = ""
            for param in parameter:
                if par != "":
                    par = par + "&"
                par = par + f"{param.lower()}={parameter[param]}"
            return url + par
        return url

    def _build_request(self, uri, method, body):
        method = method.upper()
        headers = {'Content-Type': 'application/json'}
        timest = self._make_timestamp()
        uri = self.BASE_API_URL + uri
        url = self.host + uri
        if ("/public/" in uri) or ("/push/" in uri):
            sign = self._api_short_sign(uri, timest)
            parameter = self._make_short_default_parameter(timest, sign)
        else:
            sign = self._api_sign(uri, timest)
            parameter = self._make_default_parameter(timest, sign)
#        parameter = self.set_additional_parameter(parameter, sign, timest, self.access_token)
        req = Request(method, url, headers=headers)
        if body:
            if method in ["POST", "PUT", "PATH"]:
                req.json = body
            else:
                parameter.update(body)
        req.url = self._create_parameter_url(url, parameter)
        return req

    def _build_response(self, resp):
        '''Decoding JSON - Decode json string to python object
        JSONDecodeError can happen when requests have an HTTP error code like 404 and try to parse the response as JSON
        '''

        if resp.status_code / 100 == 2:
            body = json.loads(resp.text)
        else:
            body = {"request_id": None, "error": resp.status_code, "msg": "http error code"}

        return body

        # if "error" not in body:
        #     return body
        # else:
        #     raise AttributeError(body["error"])

    def _get_cached_module(self, key):
        CACHED_MODULE = self.CACHED_MODULE.get(key)

        if not CACHED_MODULE:
            installed = self.registered_module.get(key)
            if not installed:
                return None
            CACHED_MODULE = installed(self)
            self.CACHED_MODULE.setdefault(key, CACHED_MODULE)
        return CACHED_MODULE

    def execute(self, uri, method, body=None):
        ''' defalut timeout value will be 10 seconds
        '''
        #parameter = self._make_default_parameter()
        if body.get("timeout"):
            timeout = body.get("timeout")
            body.pop("timeout")
        else:
            timeout = 10

        #if body is not None:
            #parameter.update(body)

        req = self._build_request(uri, method, body)
        print(req.params)
        print(req.url)
        prepped = req.prepare()

        s = Session()
        resp = s.send(prepped, timeout=timeout)
        resp = self._build_response(resp)
        return resp

    def _sign(self, path, timest):
        base_string = f'{self.partner_id}{path}{timest}'.encode()
        sign = hmac.new(self.partner_key.encode(), base_string, hashlib.sha256).hexdigest()
        return sign

    def auth_url(self, path):
        timest = self._make_timestamp()

        #base_string = f'{self.partner_id}{path}{timest}'.encode()
        #sign = hmac.new(self.partner_key.encode(), base_string, hashlib.sha256).hexdigest()

        sign = self._sign(path, timest)
        url = self.host + path + f'?partner_id={self.partner_id}&timestamp={timest}&sign={sign}'
        return sign, url

    def shop_authorization(self, redirect_url):
        '''
            The difference between hmac and hashlib,
            hmac uses the provided key to generate a salt and make the hash more strong, while hashlib only hashes the provided message

            In shopee partner API, shopee use hmac for general encryption while using hashlib for Authorize and CancelAuthorize module
        '''

        path = "/api/v2/shop/auth_partner"
        url = self.auth_url(path)[1] + f'&redirect={redirect_url}'
        return url

    def get_code(self):
        url = self.shop_authorization(self.redirect_url)
        browser = webdriver.Chrome('c:\\chromedriver\\chromedriver.exe')
        browser.get(url)
        while self.redirect_url not in browser.current_url:
            pass
        code = parse_url(browser.current_url).query.split('&')
        browser.close()
        self.code = code[0] = code[0].replace('code=', '')
        self.shop_id = int(code[1].replace('shop_id=', ''))
        return self.code, self.shop_id

    def get_token(self):
        body = {'code': self.code, 'shop_id': int(self.shop_id), 'partner_id': int(self.partner_id)}
        url = self.auth_url('/api/v2/auth/token/get')[1]
        headers = {'Content-Type': 'application/json'}
        resp = requests.post(url, json=body, headers=headers).json()
        print(resp)
        self.access_token = resp['access_token']
        self.refresh_token = resp['refresh_token']
        self.timeout = resp['expire_in']
        return self.access_token, self.timeout, self.refresh_token

    def get_access_token(self, shop_id, partner_id, partner_key, refresh_token):
        body = {'shop_id': int(shop_id), 'partner_id': int(partner_id), 'refresh_token': refresh_token}
        url = self.auth_url('/api/v2/auth/access_token/get')[1]
        headers = {'Content-Type': 'application/json'}
        resp = requests.post(url, json=body, headers=headers).json()
        print(resp)
        self.access_token = resp['access_token']
        self.refresh_token = resp['refresh_token']
        self.timeout = resp['expire_in']
        return self.access_token, self.timeout, self.refresh_token
