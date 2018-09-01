from .base import BaseModule


class Shop(BaseModule):

    def get_shop_info(self, **kwargs):
        """
        Use this call to get information of shop.

        :param kwargs
        :return
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

        :param kwargs
            - shop_name
            - images
            - videos
            - disable_make_offer
            - enable_display_unitno
            - shop_description
        :return
        """
        return self.client.execute("shop/update", "POST", kwargs)

    def performance(self, **kwargs):
        """
        Shop performance includes the indexes from "My Performance" of Seller Center.

        :param kwargs
        :return
        """
        return self.client.execute("shop/performance", "POST", kwargs)



    # both of the authorize and cancel_authorize should be rebuild , pending...

    # def cancel_authorize(self ,**kwargs):
    #     """
    #     Shop performance includes the indexes from "My Performance" of Seller Center.
    #     :param kwargs
    #         - redirect, string, redirect url after authorization finished.
    #         - token, string, token created by partner key and redirect. Please refer to Developer Guide
    #         - id, uint64, partner id.
    #     :return
    #     """
    #     return self.client.execute("shop/cancel_auth_partner", "POST", kwargs)


    # def authorize(self ,**kwargs):
    #     """
    #     Use this api to begin the process of authorization for a shop and a partner. 
    #     Partner should build this url with correct parameters and provide to shop owner. After call this api as GET method, user will be leaded to seller login page to validate user's permission.
    #     :param kwargs
    #         - redirect, string, redirect url after authorization finished.
    #         - token, string, token created by partner key and redirect. Please refer to Developer Guide
    #         - id, uint64, partner id.

    #     :return
    #     """
    #     return self.client.execute("shop/auth_partner", "GET", kwargs)
