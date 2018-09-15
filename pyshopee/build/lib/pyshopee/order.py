from .base import BaseModule



class Order(BaseModule):
    """
    shopee order api
    """

    def get_order_list(self, **kwargs):
        """
        GetOrdersList is the recommended call to use for order management.
        Use this call to retrieve basic information of all orders which are updated within specific period of time.
        More details of each order can be retrieved from GetOrderDetails.
        At least one time filter need to be provided.
        You can either choose create time filter or update time filter.
        For each filter you need to provice start time and end time. Ex.
        If you choose to use create time filter, you need to specify "create_time_from" and "create_time_to" in your request.
        :param kwargs:
        :return:
        """
        return self.client.execute("orders/basics", "POST", kwargs)

    def get_order_detail(self, **kwargs):
        """
        Use this call to retrieve detailed information about one or more orders based on OrderIDs.
        :param kwargs:
        :return:
        
        @@Significant OpenAPI Updates (2018-09-15/2018-07-18)
        Added pay_time field in the return parameters for order payment time.
        """


        return self.client.execute("orders/detail", "POST", kwargs)

    def get_order_escrow_detail(self, **kwargs):
        """
        Use this call to retrieve detailed escrow information about one order based on OrderID.
        :param kwargs:
        :return:
        """
        return self.client.execute("orders/my_income", "POST", kwargs)

    def get_order_by_status(self, **kwargs):
        """
        GetOrdersByStatus is the recommended call to use for order management.
        Use this call to retrieve basic information of all orders which are specific status.
        More details of each order can be retrieved from GetOrderDetails.
        :param kwargs:
        :return:

        @@Significant OpenAPI Updates (2018-09-15/2018-08-13)
        Optimized the order status can be used in the input parameter as filter for collecting the orders to initiate logistics.
        """
        return self.client.execute("orders/get", "POST", kwargs)

    def cancel_order(self, **kwargs):
        """
        Use this call to cancel an order
        :param kwargs:
        :return:
        """
        return self.client.execute("orders/cancel", "POST", kwargs)

    def accept_buyer_cancellation(self, **kwargs):
        """
        Use this call to accept buyer cancellation
        :param kwargs:
        :return:
        """
        return self.client.execute("orders/buyer_cancellation/accept", "POST", kwargs)

    def reject_buyer_cancellation(self, **kwargs):
        """
        Use this call to reject buyer cancellation
        :param kwargs:
        :return:
        """
        return self.client.execute("orders/buyer_cancellation/reject", "POST", kwargs)


