Welcome to python-shopee v1.0.0
================================
Shopee Partners API python implementation 

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
