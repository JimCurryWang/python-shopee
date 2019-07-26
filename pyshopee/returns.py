from .base import BaseModule

class Returns(BaseModule):
    """ Return Merchandise Authorization
    shopee order returns api
    """

    def confirm_return(self, **kwargs):
        """
        Confirm return
        :param kwargs:
            - returnsn: The serial number of return.
        """
        return self.client.execute("returns/confirm", "POST", kwargs)


    def dispute_return(self, **kwargs):
        """
        Dispute return
        :param kwargs:
            - returnsn: The serial number of return.
            - email: Seller's email.
            - dispute_reason : The reason for seller dispute the return. Available value: NON_RECEIPT/OTHER/NOT_RECEIVED. 
                               See Data Definition- ReturnDisputeReason
            - dispute_text_reason: The reason description for seller dispute the return.
            - images: Image URLs that seller provide. Seller can upload up 3 images at most.
        """
        return self.client.execute("returns/dispute", "POST", kwargs)


    def get_return_lists(self, **kwargs):
        """
        Get return list
        :param kwargs:
            - pagination_offset
            - pagination_entries_per_page
            - create_time_from
            - create_time_to
        """
        return self.client.execute("returns/get", "POST", kwargs)


    def get_return_detail(self, **kwargs):
        """
        Use this api to get detail information of a returned order
        :param kwargs:
            - returnsn
        """
        return self.client.execute("returns/detail", "POST", kwargs)
