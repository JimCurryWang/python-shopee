from .base import BaseModule


class Shop(BaseModule):

    def get_shop_info(self, **kwargs):
        """
        Use this call to get information of shop.

        :param kwargs:
        :return:
            - shop_id
            - shop_name
            - country
            - shop_description
            - videos
            - images
            - disable_make_offer
            - enable_display_unitno
        """
        return self.client.execute("shop/get", "POST", kwargs)

    def update_shop_info(self, **kwargs):
        """
        Use this call to update information of shop.

        :param kwargs:
            - shop_name
            - images
            - videos
            - disable_make_offer
            - enable_display_unitno
            - shop_description
        :return:
        """
        return self.client.execute("shop/update", "POST", kwargs)

    def performance(self, **kwargs):
        """
        Shop performance includes the indexes from "My Performance" of Seller Center.

        :param kwargs:
        :return:
        """
        return self.client.execute("shop/performance", "POST", kwargs)

