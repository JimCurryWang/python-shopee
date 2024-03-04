from .base import BaseModule


class Payment(BaseModule):

    def get_escrow_detail(self, **kwargs):
        """
        Use this API to fetch the accounting detail of order.
.
        :param kwargs:
         - order_sn Required

        """
        return self.client.execute("payment/get_escrow_detail", "GET", kwargs)

    def set_shop_installment_status(self, **kwargs):
        """
        Sets the staging capability of shop level.
.
        :param kwargs:
         - installment_status Required

        """
        return self.client.execute("payment/set_shop_installment_status", "POST", kwargs)

    def get_shop_installment_status(self, **kwargs):
        """
        Get the installment state of shop.

        :param kwargs:
        """
        return self.client.execute("payment/get_shop_installment_status", "GET", kwargs)

    def get_payout_detail(self, **kwargs):
        """
        Get the payoutdetail for CB.

        :param kwargs:
        - page_size Required
        - page_no Required
        - payout_time_from Required
        - payout_time_to Required

        """
        return self.client.execute("payment/get_payout_detail", "GET", kwargs)

    def set_item_installment_status(self, **kwargs):
        """
        Set item installment.Only for TH、TW.

        :param kwargs:
        - item_id_list Required
        - tenure_list Required
        """
        return self.client.execute("payment/set_item_installment_status", "POST", kwargs)

    def get_item_installment_status(self, **kwargs):
        """
        Get item installment tenures.Only for TH、TW.

        :param kwargs:
        - item_id_list Required
        """
        return self.client.execute("payment/get_item_installment_status", "POST", kwargs)

    def get_payment_method_list(self, **kwargs):
        """
        Obtain payment method (no authentication required)

        :param kwargs:
        """
        return self.client.execute("payment/get_payment_method_list", "GET", kwargs)

    def get_wallet_transaction_list(self, **kwargs):
        """
        Use this API to get the transaction records of wallet.

        :param kwargs:
        - page_no Required
        - page_size Required
        - create_time_from
        - create_time_to
        - wallet_type
        - transaction_type
        """
        return self.client.execute("payment/get_wallet_transaction_list", "GET", kwargs)

    def get_escrow_list(self, **kwargs):
        """
        Use this API to fetch the accounting list of order.

        :param kwargs:
        - release_time_from Required
        - release_time_to Required
        - page_size
        - page_no

        """
        return self.client.execute("payment/get_escrow_list", "GET", kwargs)

