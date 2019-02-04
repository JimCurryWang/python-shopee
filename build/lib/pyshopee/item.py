from .base import BaseModule


class Item(BaseModule):

    def add(self, product_data):
        """
        Use this call to add a product item. Should get dependency by calling below API first
        shopee.item.GetCategories
        shopee.item.GetAttributes
        shopee.logistics.GetLogistics
        :param product_data:
        :return:


        @@Significant OpenAPI Updates (2018-09-15/2018-08-13)
        Aligned the length of variation name with Seller Center to 20 letters.
        """
        return self.client.execute("item/add", "POST", product_data)

    def delete(self, **kwargs):
        """
        Use this call to delete a product item.
        :param kwargs:
        :return:
        """
        return self.client.execute("item/delete", "POST", kwargs)


    def unlist_item(self, **kwargs):
        """
        Use this api to unlist or list items in batch.
        :param kwargs:
            items = [
                {
                    "item_id": "Item's unique identifier"
                    "unlist": "True: unlist this item; False: list this item"
                }
            ]

        @@Significant OpenAPI Updates (2018-12-14)
        """
        return self.client.execute("items/unlist", "POST", kwargs)

    def update_item(self, update_data):
        """
        Use this call to update a product item. 
        Should get dependency by calling below API first
        
        shopee.item.GetItemDetail
        :param update_data:
        :return:
        """
        return self.client.execute("item/update", "POST", update_data)

    def update_img(self,  **kwargs):
        """
        Override and update all the existing images of an item.
        
        :params example:
            item_id = 1208720868
            images = "http://f.shopee.ph/file/805af6fd2bd978299505dac9e3c09107"
        """
        return self.client.execute("item/img/update", "POST", kwargs)

    def get_item_list(self, **kwargs):
        """
        Use this call to get a list of items
        :param kwargs:
        :return:

        @@Significant OpenAPI Updates (2018-09-15/2018-08-13)
        ​Added item_sku, variaition_id and variation_sku in the return parameters.
        """

        return self.client.execute("items/get", "POST", kwargs)

    def get_item_detail(self, **kwargs):
        """
        Use this call to get detail of item
        :param kwargs:
        :return:
        """
        return self.client.execute("item/get", "POST", kwargs)


    def update_price(self, **kwargs):
        """
        Use this call to update item price

        :param kwargs:
        :return:
        """
        return self.client.execute("items/update_price", "POST", kwargs)

    def update_stock(self, **kwargs):
        """
        Use this call to update item stock
        :param kwargs:
        :return:
        """
        return self.client.execute("items/update_stock", "POST", kwargs)

    def add_variations(self, variation_data):
        """
        Use this call to add item variations
        :param variation_data(Object[]):
            : item_id
            : name
            : stock
            : price
            : variation_sku
        :return:
        """
        return self.client.execute("item/add_variations", "POST", variation_data)

    def delete_variation(self, **kwargs):
        """
        Use this call to delete item variation
        :param kwargs:
            : item_id
            : variation_id
        :return:
        """
        return self.client.execute("item/delete_variation", "POST", kwargs)

    def update_variation_price(self, **kwargs):
        """
        Use this call to update item variation price
        :param kwargs:
        :return:
        """
        return self.client.execute("items/update_variation_price", "POST", kwargs)

    def update_variation_stock(self, **kwargs):
        """
        Use this call to update item variation stock
        :param kwargs:
        :return:
        """
        return self.client.execute("items/update_variation_stock", "POST", kwargs)


    def add_item_img(self, **kwargs):
        """
        Use this call to add product item images.

        :param kwargs:
        :return:
        """
        return self.client.execute("item/img/add", "POST", kwargs)

    def delete_item_img(self, **kwargs):
        """
        Use this call to delete a product item image.
        :param kwargs:
        :return:
        """
        return self.client.execute("item/img/delete", "POST", kwargs)


    def insert_item_img(self, **kwargs):
        """
        Use this call to add one item image in assigned position.
        :param kwargs:
        :return:
        """
        return self.client.execute("item/img/insert", "POST", kwargs)


    def get_attributes(self, **kwargs):
        """
        Use this call to get attributes of product item
        :param kwargs:
        :return:

        """
        return self.client.execute("item/attributes/get", "POST", kwargs)

    def get_categories(self, **kwargs):
        """
        Use this call to get categories of product item
        :param kwargs:
        :return:

        """
        return self.client.execute("item/categories/get", "POST", kwargs)

    def get_category_by_country(self, **kwargs):
        """
        Use this api to get categories list filtered by country and cross border without using shopID.
        :param kwargs:
            : country(String)      - Two-digit country code.
            : is_cb(uint8)         - Is cross border or not. 1: cross border; 0: not cross border

        @@Significant OpenAPI Updates (2018-09-15/2018-07-18)
        """
        return self.client.execute("item/categories/get_by_country", "POST", kwargs)


    def update_price_batch(self, **kwargs):
        """
        Update items price in batch.

        :param kwargs:
            : items(object[])  - List of items to update price. Up to 50 items in one call.
                : item_id
                : price
        @@Significant OpenAPI Updates (2018-09-15/2018-09-11)
        """
        return self.client.execute("items/update/items_price", "POST", kwargs)

    def update_stock_batch(self, **kwargs):
        """
        Update items stock in batch.

        :param kwargs:
            : items(object[])  - List of items to update stock. Up to 50 items in one call.
                : item_id
                : stock
        @@Significant OpenAPI Updates (2018-09-15/2018-09-11)
        """
        return self.client.execute("items/update/items_stock", "POST", kwargs)


    def update_variation_price_batch(self, **kwargs):
        """
        Update variations price in batch.

        :param kwargs:
            : variations(object[])  - List of variations to update price. Up to 50 variations in one call.
                : variation_id
                : price
                : item_id
        
        @@Significant OpenAPI Updates (2018-09-15/2018-09-11)
        """
        return self.client.execute("items/update/vars_price", "POST", kwargs)


    def update_variation_stock_batch(self, **kwargs):
        """
        Update variations stock in batch.

        :param kwargs:
            : variations(object[])  - List of variations to update stock. Up to 50 variations in one call.
                : variation_id
                : stock
                : item_id
        
        @@Significant OpenAPI Updates (2018-09-15/2018-09-11)
        """
        return self.client.execute("items/update/vars_stock", "POST", kwargs)




    '''
        2-Tier Variation API set(TW not live)
            item.InitTierVariation
            item.AddTierVariation
            item.GetVariations
            item.UpdateTierVariationList
            item.UpdateTierVariationIndex

        @@Significant OpenAPI Updates (2018-12-01)
    '''
    
    def InitTierVariation(self, **kwargs):
        """
        Initialize a non-tier-variation item to a tier-variation item, and initialize stock and price for each variation. 
        This API cannot edit existed tier_variation and variation price/stock.
        :param kwargs:
        """
        return self.client.execute("item/tier_var/init", "POST", kwargs)

    def AddTierVariation(self, **kwargs):
        """
        Use this api to add new tier variations in batch. 
        Tier variation index of variations in the same item must be unique.
        :param kwargs:
        """
        return self.client.execute("item/tier_var/add", "POST", kwargs)

    def GetVariations(self, **kwargs):
        """
        Use this call to get tier-variation basic information under an item.
        :param kwargs:
        """
        return self.client.execute("item/tier_var/get", "POST", kwargs)

    def UpdateTierVariationList(self, **kwargs):
        """
        Use this api to update tier-variation list of a tier-variation item.
        :param kwargs:
        """
        return self.client.execute("item/tier_var/update_list", "POST", kwargs)


    def UpdateTierVariationIndex(self, **kwargs):
        """
        Use this api to update existing tier index under the same variation_id.
        :param kwargs:
        """
        return self.client.execute("item/tier_var/update", "POST", kwargs)

