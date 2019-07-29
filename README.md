pyshopee v1.3.9
================================

[![PyPI](https://img.shields.io/badge/pypi-v1.3.7-blue.svg)](https://pypi.org/project/pyshopee/)
[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/JimCurryWang/python-shopee)
[![Depfu](https://img.shields.io/depfu/depfu/example-ruby.svg)](https://github.com/JimCurryWang/python-shopee)
  

Shopee Partners API - python implementation 
---------------------------------------------
This is Python implementation for the [Shopee Partner REST API](https://partner.test.shopeemobile.com/docs/).  

If you came here looking for the [Shopee seller center](https://seller.shopee.tw/), to shoping, then [go here](https://shopee.tw/).

```shell
$ pip install pyshopee
```

```python
import pyshopee

client = pyshopee.Client( shopid, partnerid, API_key )

# get_order_by_status (UNPAID/READY_TO_SHIP/SHIPPED/COMPLETED/CANCELLED/ALL)
resp = client.order.get_order_by_status(order_status="READY_TO_SHIP")
print(resp)


# shop authorize and cancel_authorize url
authorize_url = client.shop.authorize(redirect_url="https://shopee.tw")
print(authorize_url)

cancel_authorize_url = client.shop.cancel_authorize(redirect_url="https://shopee.tw")
print(cancel_authorize_url)
```
Features
--------
  
- Simple, reliable, and elegant.
- No need to generate authentication and timestamps by yourself, the wrapper does it for you.
- Module format functionality the same as shopee officail document.
- Good Response exception handling !

_6_ main parts of implementation
---------------------------
#### 1. Shop Management Module : [Shop](https://open.shopee.com/documents?module=6&type=1&id=410) / [ShopCategory](https://open.shopee.com/documents?module=7&type=1&id=404) 

#### 2. Orders Management Module : [Orders](https://open.shopee.com/documents?module=4&type=1&id=394)

#### 3. Logistics Management Module : [Logistics](https://open.shopee.com/documents?module=3&type=1&id=384)

#### 4. Products Management Module : [Item](https://open.shopee.com/documents?module=2&type=1&id=365) / [Image](https://open.shopee.com/documents?module=65&type=1&id=412) / [Discount](https://open.shopee.com/documents?module=1&type=1&id=357)

#### 5. RMA Management Module : [Returns](https://open.shopee.com/documents?module=5&type=1&id=401)

#### 6. Collection Management Module: [toppicks](https://open.shopee.com/documents?module=67&type=1&id=435)





Installation
-------
1. pip install from pypi
```shell
$ pip install pyshopee
```
2. clone the repository to your local folder
```shell
$ cd pyshopee
```
```shell
$ python setup.py install
```

Quick Start
-----------

#### Import pyshopee & get order by status
```python
import pyshopee

client = pyshopee.Client( shopid, partnerid, API_key )

# get_order_by_status (UNPAID/READY_TO_SHIP/SHIPPED/COMPLETED/CANCELLED/ALL)
resp = client.order.get_order_by_status(order_status="READY_TO_SHIP")
print(resp)
```
#### Get order list 

```python
# get_order_list
resp = client.order.get_order_list(create_time_from = 1512117303, create_time_to=1512635703)
print(resp)
```
#### Get order detail

```python
'''
ordersn_list , type: String[]    
The set of order IDs. You can specify, at most, 50 OrderIDs in this call.
'''
# get_order_detail
ordersn_list = [ '1712071633982A7','1712071632981JW','171207163097YCJ']
resp = client.order.get_order_detail(ordersn_list = ordersn_list )
print(resp)
```

#### Get order escrow detail
```python
'''
ordersn , type:String [] 
Shopee's unique identifier for an order.
'''
# get_order_escrow_detail
ordersn = '1712071633982A7'
resp = client.order.get_order_escrow_detail(ordersn = ordersn)
print(resp)
```


Advance Details for others functions
-------

```python
# usage
client.[type].[function name]

[type]
  - Shop
  - ShopCategory
  - Orders
  - Logistics
  - Item
  - Image
  - Discount
  - Returns
```


Developer Note
--------------
- From Aug, 2018  ShopeePartnerAPI  will change the original apply mechanism.        
Please replace with your valid parameter(shopid,partnerid,token etc.)before sumbitting the call.

- To get started, please check the [Developer Guide under Documentation](https://open.shopee.com/) - Overview - Developer Guide    
on how to become a developer and utilize Shopee OpenAPI services.

- Apply Authority Route:    
    1. Apply Developer Authority
    2. Develper Authentication
    3. Build New App's Token     
    4. Developing and Testing 
    5. Seller Authority



About testtools platform
------------------------
- The default parameters are dummies except the *PartnerID* and *Partner Key* dedicated to your APP.    
  Please replace with your valid parameter(shopid etc.) before sumbitting the call.    
- The testtools is based on PRODUCTION environment, please apply your PRODUCTION credential and parameters
  The "Request" and "Sign" tab aim to assist developer on verifying the authentication signature of API calls
  
  
  
Note
----

_Source code_  
    https://github.com/JimCurryWang/pyshopee

_pypi_    
    https://pypi.org/project/pyshopee

_Shopee Parter API Documentation_  
    https://partner.test.shopeemobile.com/docs/
    
_Registration for Shopee Partner API usage_  
    https://docs.google.com/forms/d/e/1FAIpQLSeCSsRHQSoQvZccOSHIl5DZAPIkSnS4ivN0Z6rp6N7JIoofvQ/viewform?c=0&w=1
    

