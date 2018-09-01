from .base import BaseModule


class Category(BaseModule):

    def get_categories(self, **kwargs):
        """
        Use this call to get categories of product item
        :param kwargs:
        :return:
        """
        return self.client.execute("item/categories/get", "POST", kwargs)

    def get_attributes(self, **kwargs):
        """
        Use this call to get attributes of product item
        :param kwargs:
        :return:
        """
        return self.client.execute("item/attributes/get", "POST", kwargs)

