from .base import BaseModule

class Merchant(BaseModule):
    def get_merchant_info(self, **kwargs):
        """
        Use this call to get information of merchant
.
        :param kwargs:

        """
        return self.client.execute("merchant/get_merchant_info", "GET", kwargs)

    def get_shop_list_by_merchant(self, **kwargs):
        """
        Use this call to get shop_list bound to merchant_id.
.
        :param kwargs:
         - page_no Required
         - page_size Required

        """
        return self.client.execute("merchant/get_shop_list_by_merchant", "GET", kwargs)
