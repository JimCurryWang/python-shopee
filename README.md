Welcome to python-shopee v1.1
================================
Shopee Partners API for python implementation 

This is an unofficial Python implementation for the [Shopee Partner REST API](https://partner.test.shopeemobile.com/docs/).  
The Script is in no way affiliated with Shopee, use at your own risk.

If you came here looking for the [Shopee seller center](https://seller.shopee.tw/),to purchase , then [go here](https://shopee.tw/).

_Source code_  
    https://github.com/JimCurryWang/python-shopee/

_Shopee Parter API Documentation_  
    https://partner.test.shopeemobile.com/docs/
    
_Registration for Shopee Partner API usage_  
    https://docs.google.com/forms/d/e/1FAIpQLSeCSsRHQSoQvZccOSHIl5DZAPIkSnS4ivN0Z6rp6N7JIoofvQ/viewform?c=0&w=1
    
    
Features
--------

- Implementation of Manage Orders, Manage Products and Manage Shop Accounts.  
- Simple handling of authentication  
- No need to generate timestamps yourself, the wrapper does it for you  
- Response exception handling  
- Item,Logistic,Order,Returns,Shop functionality  

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


Quick Start
-----------

```python

    from shopee.client import Client
    
    client = Client(shopid, partnerid, API_key)
    
    def test_get_order_by_status(client):
      '''get_order_by_status  
         UNPAID/READY_TO_SHIP/SHIPPED/COMPLETED/CANCELLED/ALL
      '''
        try:
            resp = client.order.get_order_by_status(order_status="READY_TO_SHIP")
            print(resp)
        except Exception as e:
            print(e)

    def test_get_order_list(client):
        resp = client.order.get_order_list(create_time_from = 1512117303, create_time_to=1512635703)
        print(resp)

    def test_get_order_detail(client):
        '''ordersn_list    String[]    
           The set of order IDs. You can specify, at most, 50 OrderIDs in this call.
        '''
        ordersn_list = [ '1712071633982A7','1712071632981JW','171207163097YCJ']
        resp = client.order.get_order_detail(ordersn_list = ordersn_list )
        print(resp)


    def test_get_order_escrow_detail():
        '''ordersn String  
           Shopee's unique identifier for an order.
        '''
        ordersn = '1712071633982A7'
        resp = client.order.get_order_escrow_detail(ordersn = ordersn)
        print(resp)

```

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



