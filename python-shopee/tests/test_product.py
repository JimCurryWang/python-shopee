# /usr/bin/env python
# -*- coding:utf8 -*-
from unittest import TestCase
import shopee
import json
import random

class TestProduct(TestCase):

    def get_client(self):
        client = shopee.Client(564, 456, "45654645")
        return client

    def test_shopee_get_item_detail(self):
        client = self.get_client()
        resp = client.product.get_item_detail(item_id=741204992)
        print(resp.status_code)
        print(resp.text)
        # 171207162767U5V

    def test_shpoee_update_variation_price_stock(self):
        client = self.get_client()
        resp = client.product.get_item_detail(item_id=741204992)

        body = json.loads(resp.text)
        print(body)
        for v in body["item"]["variations"]:
            resp = client.variation.update_price(item_id=741204992, variation_id=v["variation_id"], price=99999)
            print(resp.text)
            resp = client.variation.update_stock(item_id=741204992, variation_id=v["variation_id"], stock=999)
            print(resp.text)


    def test_shopee_update_product(self):
        client = self.get_client()
        category_id = 7606

        resp = client.category.get_attributes(category_id=category_id)
        body = json.loads(resp.text)

        attributes = []
        for i in body["attributes"]:

            if i["is_mandatory"]:

                if i['options'] and i["input_type"] != "COMBO_BOX":
                    value = random.sample(i['options'], 1)
                else:
                    value = " "

                attributes.append({
                    "attributes_id": i["attribute_id"],
                    "value": value
                })

        update_data = {

            "item_id": 741204992,
            "category_id": 7606,
            "attributes": attributes
        }

        print(update_data)
        resp = client.product.update(update_data)
        print(resp.text)


    def test_shopee_delete_product(self):
        client = self.get_client()
        resp = client.product.delete(item_id=741204992)
        print(resp.text)


    def test_shopee_update_price_stock(self):
        client = self.get_client()
        resp = client.product.update_price(item_id=741204992, price = 99999)
        print(resp.text)
        resp = client.product.update_stock(item_id=741204992, stock = 99999)
        print(resp.status_code)
        print(resp.text)

    def test_shopee_insert_item_img(self):
        client = self.get_client()
        resp = client.product.insert_item_img(item_id=741204992, image_url="http://xxxx.xxxx.com/image/187536/normal/187536-3.jpg", image_position=1)
        print(resp.text)

    def test_shopee_product_add(self):
        client = self.get_client()
        resp = client.category.get_categories()

        category_id = 7606

        resp = client.category.get_attributes(category_id = category_id)
        body = json.loads(resp.text)

        attributes = []
        for i in body["attributes"]:
            if i["is_mandatory"]:
                if i['options'] and i["input_type"] != "COMBO_BOX":
                    value = random.sample(i['options'], 1)
                else:
                    value = "N/A"
                attributes.append({
                        "attributes_id": i["attribute_id"],
                        "value": value
                    })

        logistics = []

        resp = client.logistic.get_logistics()
        body = json.loads(resp.text)

        for i in body["logistics"]:
            if i["enabled"]:
                logistics.append({
                    "logistic_id": i["logistic_id"],
                    "enabled": True
                })

        wholesales = [
            {
                "min": 5,
                "max": 10,
                "unit_price": 998
            }
        ]
        images = [
            {
                "url": "http://xxx.xxx.com/image/187536/normal/187536-2.jpg"
            }
        ]
        variations = [
            {
                "name": "Black",
                "stock": 1000,
                "price": 1999,
                "variation_sku": "SKU-ABCD-EFG0-002"
            },
            {
                "name": "Red",
                "stock": 1000,
                "price": 2999,
                "variation_sku": "SKU-ABCD-EFG0-003"
            }
        ]
        product_data = {
            "category_id": category _id,
            "name": "Shopee API Test",
            "description": "Shopee API Test",
            "price": 1000,
            "stock": 999,
            "item_sku": "SKU-ABCD-EFG0-HIJK",
            "variations":variations,
            "images":images,
            "attributes":attributes,
            "logistics": logistics,
            "weight": 1000,
            "package_length": 200,
            "package_width": 200,
            "package_height": 200,
            "days_to_ship": 10,
            "wholesales": wholesales
        }


        resp = client.product.add(product_data)

        print(resp.text)
