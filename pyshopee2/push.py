from .base import BaseModule


class Push(BaseModule):
    def get_push_config(self, **kwargs):
        """
            get the configuration information of push service


        :param kwargs
        :return
        https://open.shopee.com/documents?module=105&type=1&id=665&version=2
        """
        return self.client.execute("push/get_push_config", "GET", kwargs)

    def set_push_config(self, **kwargs):
        """
        Use this API to set the configuration information of push service.


        :param kwargs
            - callback_url
            - push_config
                - order_status
                - order_tracking_no
                - shop_update
                - banned_item
                - itme_promotion
                - reserved_stock_change
                - webchat
            - blocked_shop_id
        :return
        https://open.shopee.com/documents?module=105&type=1&id=666&version=2
        """
        return self.client.execute("push/set_push_config", "POST", kwargs)