from .base import BaseModule


class ShopCategory(BaseModule):

    def add_shop_category(self, **kwargs):
        """
        Use this call to add a new collecion

        :param kwargs:
            : name (Required)                     - ShopCategory's name.
            : sort_weight(not Required) - ShopCategory's sort weight.
        """
        return self.client.execute("shop_category/add_shop_category", "POST", kwargs)

    def get_shop_category_list(self, **kwargs):
        """
        Use this call to get list of shop categories

        :param kwargs:
            : page_size (Required)
            : page_no  (Required)
        """
        return self.client.execute("shop_categorys/get_shop_category_list", "GET", kwargs)

    def delete_shop_category(self, **kwargs):
        """
        Use this call to delete a existing shop collecion

        :param kwargs:
            : shop_category_id (Required) - ShopCategory's unique identifier.
        """
        return self.client.execute("shop_category/delete_shop_category", "POST", kwargs)

    def update_shop_category(self, **kwargs):
        """
        Use this call to update a existing collecion

        :param kwargs:
            : shop_category_id   (Required)        - ShopCategory's unique identifier.
            : name                                 - ShopCategory's name.
            : sort_weight                          - ShopCategory's sort weight.
            : status                               - ShopCategory's status. Applicable values: NORMAL, INACTIVE, DELETED.
        """
        return self.client.execute("shop_category/update_shop_category", "POST", kwargs)

    def add_item_list(self, **kwargs):
        """
        Use this call to add items list to certain shop_category

        :param kwargs:
            : shop_category_id  (Required)- ShopCategory's unique identifier.
            : items            (Required) - Shopee's unique identifiers list for an item.
        """
        return self.client.execute("shop_category/add_item_list", "POST", kwargs)

    def get_item_list(self, **kwargs):
        """
        Use this call to get items list of certain shop_category

        :param kwargs:
            : shop_category_id (Required) - ShopCategory's unique identifier.
            : page_size
            : page_no
        """
        return self.client.execute("shop_category/get_item_list", "GET", kwargs)

    def delete_item_list(self, **kwargs):
        """
        Use this api to delete items from shop category

        :param kwargs:
            : shop_category_id  (Required)- ShopCategory's unique identifier.
            : items            (Required) - Shopee's unique identifiers list for an item.
        """
        return self.client.execute("shop_category/delete_item_list", "POST", kwargs)
