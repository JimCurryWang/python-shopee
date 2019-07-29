import pyshopee
import re
import pandas as pd 
from pprint import pprint


def _builder_attributes(attributes_resp, brand_option = None, default_brand_option = "自有品牌"):
    '''select mandatory attr.
    
    attributes =  [
                    {
                        'attributes_id': 1365,
                        'value': 'Napla(娜普菈)'
                    }
                ]
    '''
    attributes = []

    # in case attributes response is not define in api response
    if attributes_resp.get("attributes"):

        for ele in attributes_resp.get("attributes"):
            if ele.get("is_mandatory") and ele.get("attribute_name")=='品牌':
                attributes.append(
                    { 
                        "attributes_id": ele.get("attribute_id"),
                        "value": brand_option if brand_option else default_brand_option
                    })
            elif ele.get("is_mandatory"):
                attributes.append(
                    { 
                        # checking the value if value can radom or set as " "
                        "attributes_id": ele.get("attribute_id"),
                        "value": ele.get("options")[0] if len(ele.get("options")) > 0 else " ",
                    })
            else:
                pass
    else:
        return None

    return attributes

def _builder_logistics(**params):
    '''
    logistics = [
              # 'logistic_name': '黑貓宅急便'
              {
                'logistic_id': 30001,
                'enabled':False
              },
              # 'logistic_name': '7-11',
              {
                'logistic_id': 30005, 
                'enabled':False
               },
              # 'logistic_name': '全家',
              {
                'logistic_id': 30006, 
                'enabled':False
              },
              # 'logistic_name': '萊爾富',
              {
                'logistic_id': 30007, 
                'enabled':False
              },
              # 'logistic_name': 'OK Mart',
              {
                'logistic_id': 30008, 
                'enabled':False
               },
              # 'logistic_name': '中華郵政',
              {
                'logistic_id': 39303, 
                'enabled':False
              },
              # 'logistic_name': '賣家宅配',
              {
                'logistic_id': 39304, 
                'enabled':False
              },
              # 'logistic_name': '宅配',
              {
                'logistic_id': 39307, 
                'enabled':True
               }
    ]
    '''

    logistics = list()

    resp = shopee.logistic.get_logistics()

    logistics_resp = resp.get("logistics")
    for logis in logistics_resp:
        if logis.get('enabled'):
            # logistics.append({ 
            #     'logistic_id': logis.get('logistic_id'),
            #     'enabled': logis.get('enabled') 
            # })
            if logis.get('fee_type') == 'SIZE_SELECTION':
                logis['sizes'] = logis['sizes'][0]['size_id']
            else:
                logistics.append(logis)

    return logistics

def _builder_images(single, **params):
    '''
        images = [
            {
                "url": "https://cfshopeetw-a.akamaihd.net/file/b77c9b16ec1dd734c0c663fd1fcb8ac0"
            },
            {
                "url": 'https://cfshopeetw-a.akamaihd.net/file/b77c9b16ec1dd734c0c663fd1fcb8ac0'
            },
            {
                "url": 'https://cfshopeetw-a.akamaihd.net/file/b77c9b16ec1dd734c0c663fd1fcb8ac0'
            },
            {
                "url": 'https://cfshopeetw-a.akamaihd.net/file/b77c9b16ec1dd734c0c663fd1fcb8ac0'
            }
        ]
    '''
    images_container = []
    images_container.extend( single.get("images").split(",") )

    images = []
    for img in images_container:
        images.append(
            {
                "url": "https://cfshopeetw-a.akamaihd.net/file/" + str(img)
            }
        )

    return images


def _builder_variations(data, **params):
    '''
        variations = [
            {
                "name": "Black",
                "stock": 1,
                "price": 1999.0,
                "variation_sku": "SKU-ABCD-EFG0-002"
            },
            {
                "name": "Red",
                "stock": 1,
                "price": 2999.0,
                "variation_sku": "SKU-ABCD-EFG0-003"
            }
        ]
    '''
    multi = len(data) if len(data) > 1 else None
    
    variations_container = []
    if multi:
        for ele in data:

            variations = {}

            # check
            if ele["modelid"] == 0 or ele["model_status"] == 0:
                pass
            else:   
                variations.setdefault("name",ele["model_name"].strip())
                variations.setdefault("stock",1)
                variations.setdefault("price",ele["model_price"])
                if ele.get("variation_sku"):
                    variations.setdefault("variation_sku",ele.get("variation_sku"))

                variations_container.append(variations)
        return variations_container
    
    else:
        return None


def _builder_weight(single, default_weight=0.1, **params):
    ''' the net weight of this item, the unit is KG.
    - type: float
    - require: yes
    '''
    if single.get("item_weight"):
        weight = single.get("item_weight")/100000 
    else:
        weight = default_weight
    
    return float(weight)



def _cleaning_hashtag(description, **params):
    hashtag_pattern = re.compile(r"#(.*)[\s]{0,1}", flags=re.UNICODE)
    cleaned_description = hashtag_pattern.sub(r' ', description)

    return cleaned_description






if __name__ == '__main__':

    # build the connection
    shopee = pyshopee.Client( shop_id= your_shopid, 
                              partner_id=your_partner_id, 
                              secret_key=your_secret_key ) 



    # build your data in here 
    single = {
        "category_id":category_id,
        "item_name":item_name,
        "descriptio":descriptio,
        "item_price":item_price,
        "item_weight":item_weight,
        "category_id":category_id,
        "images":images
    }

    product_data = {
            "category_id": single.get("category_id"),
            "name": single.get("item_name").strip(),
            "description": _cleaning_hashtag(description =single.get("description") ),
            "price": single.get("item_price") if single.get("item_price") > 0 else data[1].get("item_price"),
            "stock": 1,
            "weight": _builder_weight(single=single, default_weight=0.1),

            # "variations": variations,
            "images": _builder_images(single=single),
            # "attributes": _builder_attributes( attributes_resp = shopee.item.get_attributes(category_id=int(single["category_id"])),
            #                                    brand_option = single.get("value"),
            #                                    default_brand_option = "自有品牌" ),
            "logistics": _builder_logistics(),
            
            # "package_length": 200,
            # "package_width": 200,
            # "package_height": 200,
            # "days_to_ship": 10,
            # "wholesales": wholesales
        }

    attributes = _builder_attributes( attributes_resp = shopee.item.get_attributes(category_id=int(single["category_id"])),
                                      brand_option = single.get("value"),
                                      default_brand_option = "自有品牌" )
    if attributes:
        product_data.setdefault("attributes",attributes)


    variations =  _builder_variations(data=data)
    if variations:
        product_data.setdefault("variations",variations)

    

    # adding process
    response = shopee.item.add(product_data=product_data)

    pprint(response)