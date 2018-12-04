from .base import BaseModule


class Public(BaseModule):
    '''
        @@Significant OpenAPI Updates (2018-12-01)
    '''

    def get_shops_by_partner(self, **kwargs):
        """
        Use this call to get basic info of shops which have authorized to the partner.

        :param kwargs
            - partner_id

        :return
            - authed_shops
                - country
                - shopid
                - auth_time
            - request_id

        """
        return self.client.execute("shop/get_partner_shop", "POST", kwargs)

    def get_categories_by_country(self, **kwargs):
        """
        Use this api to get categories list filtered by country and cross border without using shopID.

        :param kwargs
            - country
            - is_cb
            - language
        :return
        """
        return self.client.execute("item/categories/get_by_country", "POST", kwargs)

    def get_payment_list(self, **kwargs):
        """
        The supported payment method list by country

        :param kwargs
        :return
        """
        return self.client.execute("payment/list", "POST", kwargs)
