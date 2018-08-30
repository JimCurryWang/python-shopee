from .base import BaseModule


class Product(BaseModule):

    def add(self, product_data):
        """
        Use this call to add a product item. Should get dependency by calling below API first
        shopee.item.GetCategories
        shopee.item.GetAttributes
        shopee.logistics.GetLogistics
        :param product_data:
        :return:
        """
        return self.client.execute("item/add", "POST", product_data)

    def add_item_img(self, **kwargs):
        """
        Use this call to add product item images.

        :param kwargs:
        :return:
        """
        return self.client.execute("item/img/add", "POST", kwargs)

    def delete(self, **kwargs):
        """
        Use this call to delete a product item.
        :param kwargs:
        :return:
        """
        return self.client.execute("item/delete", "POST", kwargs)

    def delete_item_img(self, **kwargs):
        """
        Use this call to delete a product item image.
        :param kwargs:
        :return:
        """
        return self.client.execute("item/img/delete", "POST", kwargs)

    def get_item_detail(self, **kwargs):
        """
        Use this call to get detail of item
        :param kwargs:
        :return:
        """
        return self.client.execute("item/get", "POST", kwargs)

    def get_item_list(self, **kwargs):
        """
        Use this call to get a list of items
        :param kwargs:
        :return:
        """
        return self.client.execute("items/get", "POST", kwargs)

    def update(self, update_data):
        """
        Use this call to update a product item. Should get dependency by calling below API first
        shopee.item.GetItemDetail
        :param update_data:
        :return:
        """
        return self.client.execute("item/update", "POST", update_data)

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

    def insert_item_img(self, **kwargs):
        """
        Use this call to add one item image in assigned position.
        :param kwargs:
        :return:
        """
        return self.client.execute("item/img/insert", "POST", kwargs)
