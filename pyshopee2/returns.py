from .base import BaseModule


class Returns(BaseModule):
    def get_return_detail(self, **kwargs):
        """
            Use this api to get detail information of a return by return id.

        :param kwargs
            - return_sn  (Required)
        :return
        https://open.shopee.com/documents?module=102&type=1&id=607&version=2
        """
        return self.client.execute("sellerchat/get_return_detail", "GET", kwargs)

    def get_return_list(self, **kwargs):
        """
            Use this api to get detail information of many return by shop id.

        :param kwargs
            - page_no (Required)
            - page_size  (Required)
            - create_time_from
            - create_time_to
        :return
        https://open.shopee.com/documents?module=102&type=1&id=608&version=2
        """
        return self.client.execute("sellerchat/get_return_list", "GET", kwargs)

    def confirm(self, **kwargs):
        """
            Confirm return

        :param kwargs
            - return_sn  (Required)
        :return
        https://open.shopee.com/documents?module=102&type=1&id=609&version=2
        """
        return self.client.execute("sellerchat/confirm", "POST", kwargs)

    def dispute(self, **kwargs):
        """
            Confirm return

        :param kwargs
            - return_sn  (Required)
            - email
            - dispute_reason
            - dispute_text_reason
            - image
        :return
        https://open.shopee.com/documents?module=102&type=1&id=609&version=2
        """
        return self.client.execute("sellerchat/dispute", "POST", kwargs)