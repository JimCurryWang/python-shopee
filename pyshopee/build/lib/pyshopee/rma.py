from .base import BaseModule



class RMA(BaseModule):
    """ Return Merchandise Authorization
    shopee order returns api
    """
    def confirm_return(self, **kwargs):
        """
        Confirm return
        :param kwargs:
        :return:
        """
        return self.client.execute("returns/confirm", "POST", kwargs)

    def dispute_return(self, **kwargs):
        """
        Dispute return
        :param kwargs:
        :return:
        """
        return self.client.execute("returns/dispute", "POST", kwargs)

    def get_return_list(self, **kwargs):
        """
        Get return list
        :param kwargs:
        :return:
        """
        return self.client.execute("returns/get", "POST", kwargs)
