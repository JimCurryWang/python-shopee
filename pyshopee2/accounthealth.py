from .base import BaseModule


class AccountHealth(BaseModule):
    def shop_performance(self, **kwargs):
        """
            The data metrics of shop performance


        :param kwargs
        :return

        """
        return self.client.execute("account_health/shop_performance", "GET", kwargs)

    def shop_penalty(self, **kwargs):
        """
            To get the information of shop penalty.


        :param kwargs
        :return

        """
        return self.client.execute("account_health/shop_penalty", "GET", kwargs)