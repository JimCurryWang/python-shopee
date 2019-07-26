from .base import BaseModule



class RMA(BaseModule):
    """ Return Merchandise Authorization
    shopee order returns api

    Warning: This class will be depreciate soon
    """
    def confirm_return(self, **kwargs):
        """
        Confirm return
        :param kwargs:
        :return:
        """
        warnings.warn('Class RMA will be replaced by Class returns', DeprecationWarning)
        return self.client.execute("returns/confirm", "POST", kwargs)

    def dispute_return(self, **kwargs):
        """
        Dispute return
        :param kwargs:
        :return:
        """
        warnings.warn('Class RMA will be replaced by Class returns', DeprecationWarning)
        return self.client.execute("returns/dispute", "POST", kwargs)

    def get_return_list(self, **kwargs):
        """
        Get return list
        :param kwargs:
        :return:
        """
        warnings.warn('Class RMA will be replaced by Class returns', DeprecationWarning)
        return self.client.execute("returns/get", "POST", kwargs)
