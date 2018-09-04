pyshopee v1.2.1
================================

[![PyPI](https://img.shields.io/badge/pypi-v1.2.2-blue.svg)](https://pypi.org/project/pyshopee/)
[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/JimCurryWang/python-shopee)
[![Depfu](https://img.shields.io/depfu/depfu/example-ruby.svg)](https://github.com/JimCurryWang/python-shopee)
 

Shopee Partners API - python implementation 
---------------------------------------------
This is Python implementation for the [Shopee Partner REST API](https://partner.test.shopeemobile.com/docs/).  

If you came here looking for the [Shopee seller center](https://seller.shopee.tw/),to purchase , then [go here](https://shopee.tw/).

_Source code_  
    https://github.com/JimCurryWang/python-shopee/

_pypi_    
    https://pypi.org/project/pyshopee

_Shopee Parter API Documentation_  
    https://partner.test.shopeemobile.com/docs/
    
_Registration for Shopee Partner API usage_  
    https://docs.google.com/forms/d/e/1FAIpQLSeCSsRHQSoQvZccOSHIl5DZAPIkSnS4ivN0Z6rp6N7JIoofvQ/viewform?c=0&w=1
    
    
Features
--------

- Implementation of Manage Orders, Manage Products and Manage Shop Accounts.  
- Simple handling of authentication  
- No need to generate timestamps yourself, the wrapper does it for you.
- Good Response exception handling.
- Item, Logistic, Order, Returns, Shop module functionality.
- New feature will keep maintaining !

Developer Note
--------------
- From Aug, 2018  ShopeePartnerAPI  will change the original apply mechanism.        
Please replace with your valid parameter(shopid,partnerid,token etc.)before sumbitting the call.

- To get started, please check the [Developer Guide under Documentation](https://open.shopee.com/) - Overview - Developer Guide    
on how to become a developer and utilize Shopee OpenAPI services.

- Apply Authority Route:    
    Apply Developer Authority → Develper Authentication → Build New App's Token →     
    Developing and Testing → Seller Authority



About testtools platform
------------------------
- The default parameters are dummies except the *PartnerID* and *Partner Key* dedicated to your APP.    
  Please replace with your valid parameter(shopid etc.) before sumbitting the call.    
- The testtools is based on PRODUCTION environment, please apply your PRODUCTION credential and parameters
  The "Request" and "Sign" tab aim to assist developer on verifying the authentication signature of API calls
  

Install
-------
1. pip install from pypi
```shell
$ pip install pyshopee
```
2. clone the repository to your local folder
```shell
$ cd python-shopee
```
```shell
$ python setup.py install
```

Quick Start
-----------

#### import pyshopee & get order by status
```python
import pyshopee

client = pyshopee.Client( shopid, partnerid, API_key )

# get_order_by_status
# UNPAID/READY_TO_SHIP/SHIPPED/COMPLETED/CANCELLED/ALL
resp = client.order.get_order_by_status(order_status="READY_TO_SHIP")
print(resp)
```
#### get order list 

```python
# get_order_list
resp = client.order.get_order_list(create_time_from = 1512117303, create_time_to=1512635703)
print(resp)
```
#### get order detail

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

#### get order escrow detail
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
```

#### 1. client.category
    - get_categories(**kwargs)
    
    - get_attributes(**kwargs)
#### 2. client.logistic
    - get_logistics()
        - Use this call to get all supported Logistic Channel
        
    - get_address()
        - Use this call to get all required param for init logistic.
        
    - get_airway_bill(**kwargs)
         - Use this API to get airway bill for orders
         
    - get_branch(**kwargs)
         - Use this call to get all required param for init logistic.
         
    - get_logistic_message(**kwargs)
        - Use this call to get the logistics tracking information of an order.
        
    - get_order_logistic(**kwargs)
        - Use this call to fetch the logistics information of an order, these info can be used for waybill printing.
        
    - get_parameter_for_init(**kwargs)
        - Use this call to get all required param for init logistic.
        
    - get_time_slot(**kwargs)
        - Use this call to get all required param for init logistic.
        
    - get_tracking_no(**kwargs)
        - Use this API to get tracking number of orders
        
    - init(**kwargs)
        - Use this call to arrange Pickup or Dropoff. Should call shopee.logistics.GetParameterForInit to fetch all required param first.
        
    - set_logistic_status(**kwargs)
        - Set Logistic Status to PICKUP_DONE, this API only works for non-integrated logistic channels
        
    - set_tracking_no(**kwargs)
        - User this call to set tracking number for each order in batch.
    
#### 3. client.order
    - get_order_list(**kwargs)
        - GetOrdersList is the recommended call to use for order management.
        
    - get_order_detail(**kwargs):
        - Use this call to retrieve detailed information about one or more orders based on OrderIDs.
        
    - get_order_escrow_detail(**kwargs):
        - Use this call to retrieve detailed escrow information about one order based on OrderID.
        
    - get_order_by_status(**kwargs):
        - GetOrdersByStatus is the recommended call to use for order management.
        
    - cancel_order(**kwargs):
        - Use this call to cancel an order
        
    - accept_buyer_cancellation(**kwargs):
        - Use this call to accept buyer cancellation
        
    - reject_buyer_cancellation(**kwargs):
        - Use this call to reject buyer cancellation
        
#### 4. client.product
    - add(product_data)
        - Use this call to add a product item. Should get dependency by calling below API first

    - add_item_img(**kwargs)
        - Use this call to add product item images.
        
    - delete(**kwargs)
        - Use this call to delete a product item.

    - delete_item_img(**kwargs)
        - Use this call to delete a product item image.

    - get_item_detail(**kwargs)
        - Use this call to get detail of item

    - get_item_list(**kwargs)
        - Use this call to get a list of items

    - update(update_data)
        - Use this call to update a product item. Should get dependency by calling below API first
        
    - update_price(**kwargs)
        - Use this call to update item price

    - update_stock(**kwargs)
        - Use this call to update item stock
    
    - insert_item_img(**kwargs)
        - Use this call to add one item image in assigned position.
    
#### 5. client.rma
    - confirm_return(**kwargs)
        - Confirm return
        
    - dispute_return(**kwargs)
        - Dispute return
        
    - get_return_list(**kwargs)
        - Get return list
    
#### 6. client.shop
    - get_shop_info(**kwargs):
        - Use this call to get information of shop.
    - update_shop_info(**kwargs):
        - Use this call to update information of shop.
    - performance(**kwargs):
        - Shop performance includes the indexes from "My Performance" of Seller Center.

#### 7. client.variation
    - add(variation_data)
        - Use this call to add item variations

    - delete(**kwargs)
        - Use this call to delete item variation

    - update_price(**kwargs)
        - Use this call to update item variation price

    - update_stock(**kwargs)
        - Use this call to update item variation stock

Publish History
--------
- 20180214 ShopeePartnerAPI main function building.  
- 20180714 Add new class method - shop    
This class can get information or update information of shop ,and get shop performance includes the indexes from "My Performance" of Seller Center.


To Be Announce
--------
New API
- shopee.shop.Performance
Shop performance includes the indexes from "My Performance" of Seller Center.

- shopee.item.GetCategoriesByCountry
Use this api to get categories list filtered by country and cross border without using shopID. 3rd-party vendor should find it easier to store category without using a specific shopID.

- Optimized API
shopee.orders.GetOrderDetails
Added pay_time field in the return parameters for order payment time.

