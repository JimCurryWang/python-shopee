import pyshopee
from pprint import pprint

# shopee reg
# shopee = pyshopee.Client(shop_id =50662979, partner_id = 840616, secret_key = "3bf09f91f5deba2eb86e3cd056f37aa5cc525d57a38c202a067aef95833304e6")

# shopee24
shopee = pyshopee.Client(shop_id = 37137599, partner_id = 840210, secret_key = '58d8d9e147f788234ee2a0300c0ca0b5ff191cb8e54031b052ad4afb6176c123')

# response = shopee.shop.get_shop_info(timeout=10)
# response = shopee.shop.authorize()
# response = shopee.shop.cancel_authorize()
# # response = shopee.item.get_item_detail(item_id=1587839166)

response = shopee.logistic.get_logistics(timeout=15)
print(response)

shopee.unittest()

