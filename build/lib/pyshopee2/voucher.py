from .base import BaseModule


class Voucher(BaseModule):

    def add_voucher(self, **kwargs):
        """
        Add voucher
.
        :param kwargs:

        """
        return self.client.execute("voucher/add_voucher", "POST", kwargs)

    def delete_voucher(self, **kwargs):
        """
        Delete voucher
.
        :param kwargs:

        """
        return self.client.execute("voucher/delete_voucher", "POST", kwargs)

    def end_voucher(self, **kwargs):
        """
        End Voucher

        :param kwargs:
        - item_id_list Required

        """
        return self.client.execute("voucher/end_voucher", "POST", kwargs)

    def update_voucher(self, **kwargs):
        """
        Update voucher

        :param kwargs:

        """
        return self.client.execute("voucher/update_voucher", "POST", kwargs)

    def get_voucher_detail(self, **kwargs):
        """
        Get voucher detail.

        :param kwargs:

        """
        return self.client.execute("voucher/get_voucher_detail", "GET", kwargs)

    def get_voucher_list(self, **kwargs):
        """
        Get Voucher List.

        :param kwargs:
        """
        return self.client.execute("voucher/get_voucher_list", "GET", kwargs)
