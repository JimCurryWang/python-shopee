from .base import BaseModule


class Shop(BaseModule):

    def get_shop_info(self, **kwargs):
        """
        Use this call to get information of shop

        :param kwargs
        :return

        """
        return self.client.execute("shop/get_shop_info", "GET", kwargs)

    def get_profile(self, **kwargs):
        """
        This API support to get information of shop.

        :param kwargs
        :return

        """
        return self.client.execute("shop/get_profile", "GET", kwargs)

    def update_profile(self, **kwargs):
        """
        Use this call to update information of shop.

        :param kwargs
            - shop_name
            - shop_logo
            - description
        :return
        """
        return self.client.execute("shop/update_profile", "POST", kwargs)


