from .base import BaseModule


class Variation(BaseModule):

    def add(self, variation_data):
        """
        Use this call to add item variations
        :param variation_data:
        :return:
        """
        return self.client.execute("item/add_variations", "POST", variation_data)

    def delete(self, **kwargs):
        """
        Use this call to delete item variation
        :param kwargs:
        :return:
        """
        return self.client.execute("item/delete_variation", "POST", kwargs)

    def update_price(self, **kwargs):
        """
        Use this call to update item variation price
        :param kwargs:
        :return:
        """
        return self.client.execute("items/update_variation_price", "POST", kwargs)

    def update_stock(self, **kwargs):
        """
        Use this call to update item variation stock
        :param kwargs:
        :return:
        """
        return self.client.execute("items/update_variation_stock", "POST", kwargs)
