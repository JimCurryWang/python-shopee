import hmac
import time
import requests
import hashlib
from selenium import webdriver
from urllib3.util import parse_url

class Client20:

    def __init__(self, partner_id, partner_key, redirect_url, host ='https://partner.uat.shopeemobile.com'):

        self.partner_id = partner_id
        self.partner_key = partner_key
        self.redirect_url = redirect_url
        self.host = host
        self.shop_id = None
        self.code = None
        self.access_token = None
        self.refresh_token = None
    
    def auth_url(self, path):

        timest = int(time.time())
        base_string = f'{self.partner_id}{path}{timest}'.encode()
        sign = hmac.new(self.partner_key.encode(), base_string, hashlib.sha256).hexdigest()
        url = self.host + path + f'?partner_id={self.partner_id}&timestamp={timest}&sign={sign}'
        return url


    def get_code(self):

        url = self.auth_url('/api/v2/shop/auth_partner') + f'&redirect={self.redirect_url}'
        browser = webdriver.Firefox()
        print(url)
        browser.get(url)
        while self.redirect_url not in browser.current_url:
            pass
        browser.close()
        code = parse_url(browser.current_url).query.split('&')
        self.code = code[0] = code[0].replace('code=', '')
        self.shop_id = int(code[1].replace('shop_id=', ''))
        return self.code, self.shop_id


    def get_token(self):
        
        body = {'code': self.code, 'shop_id': self.shop_id, 'partner_id': self.partner_id}
        url = self.auth_url('/api/v2/auth/token/get')
        headers = {'Content-Type': 'application/json'}
        resp = requests.post(url, json=body, headers=headers).json()
        self.access_token = resp['access_token']
        self.refresh_token = resp['refresh_token']
        return self.access_token, self.refresh_token

    def get_access_token(self, shop_id, partner_id, partner_key, refresh_token):
        
        body = {'shop_id': shop_id, 'partner_id': partner_id, 'refresh_token': refresh_token}
        url = self.auth_url('/api/v2/auth/access_token/get')
        headers = {'Content-Type': 'application/json'}
        resp = requests.post(url, json=body, headers=headers).json()
        self.access_token = resp['access_token']
        self.refresh_token = resp['refresh_token']
        return self.access_token, self.refresh_token