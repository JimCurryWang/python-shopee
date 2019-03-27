from .base import BaseModule


class ShopCategory(BaseModule):
    '''@@Significant OpenAPI Updates (2018-09-15/2018-??-??)
    '''

    def add_items(self, **kwargs):
        """
        Use this call to add items list to certain shop_category

        :param kwargs:
            : shop_category_id - ShopCategory's unique identifier.
            : items            - Shopee's unique identifiers list for an item.
        """
        return self.client.execute("shop_category/add/items", "POST", kwargs)


    def delete_shop_category(self, **kwargs):
        """
        Use this call to delete a existing collecion

        :param kwargs:
            : shop_category_id - ShopCategory's unique identifier.
        """
        return self.client.execute("shop_category/delete", "POST", kwargs)


    def add_shop_category(self, **kwargs):
        """
        Use this call to add a new collecion

        :param kwargs:
            : name                      - ShopCategory's name.
            : sort_weight(not Required) - ShopCategory's sort weight.
        """
        return self.client.execute("shop_category/add", "POST", kwargs)


    def get_items(self, **kwargs):
        """
        Use this call to get items list of certain shop_category

        :param kwargs:
            : shop_category_id - ShopCategory's unique identifier.
        """
        return self.client.execute("shop_category/get/items", "POST", kwargs)


    def get_shop_categories(self, **kwargs):
        """
        Use this call to get list of in-shop categories

        :param kwargs:
            : pagination_offset 
            : pagination_entries_per_page
        """
        return self.client.execute("shop_categorys/get", "POST", kwargs)

    def update_shop_category(self, **kwargs):
        """
        Use this call to update a existing collecion

        :param kwargs:
            : shop_category_id          - ShopCategory's unique identifier.
            : name(not Required)        - ShopCategory's name.
            : sort_weight(not Required) - ShopCategory's sort weight.
            : status(not Required)      - ShopCategory's status. Applicable values: NORMAL, INACTIVE, DELETED.
        """
        return self.client.execute("shop_category/update", "POST", kwargs)



