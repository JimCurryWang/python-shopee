from .base import BaseModule


class Logistic(BaseModule):
    """
        shopee Logistic api
    """

    def get_logistics(self):
        """
        Use this call to get all supported Logistic Channel
        :return:
        """
        return self.client.execute("logistics/channel/get", "POST")

    def get_address(self):
        """
        Use this call to get all required param for init logistic.
        :return:
        """
        return self.client.execute("logistics/address/get", "POST")

    def get_airway_bill(self, **kwargs):
        """
        Use this API to get airway bill for orders
        :param kwargs:
        :return:
        """
        return self.client.execute("logistics/airway_bill/get_mass", "POST", kwargs)

    def get_branch(self, **kwargs):
        """
        Use this call to get all required param for init logistic.
        :param kwargs:
        :return:
        """
        return self.client.execute("logistics/branch/get", "POST", kwargs)

    def get_logistic_message(self, **kwargs):
        """
        Use this call to get the logistics tracking information of an order.

        :param kwargs:
        :return:
        """
        return self.client.execute("logistics/tracking", "POST", kwargs)

    def get_order_logistic(self, **kwargs):
        """
        Use this call to fetch the logistics information of an order, these info can be used for waybill printing.
        :param kwargs:
        :return:
        """
        return self.client.execute("logistics/order/get", "POST", kwargs)

    def get_parameter_for_init(self, **kwargs):
        """
        Use this call to get all required param for init logistic.
        :param kwargs:
        :return:
        """
        return self.client.execute("logistics/init_parameter/get", "POST", kwargs)

    def get_time_slot(self, **kwargs):
        """
        Use this call to get all required param for init logistic.
        :param kwargs:
        :return:
        """
        return self.client.execute("logistics/timeslot/get", "POST", kwargs)

    def get_tracking_no(self, **kwargs):
        """
        Use this API to get tracking number of orders

        :param kwargs:
        :return:
        """
        return self.client.execute("logistics/tracking_number/get_mass", "POST", kwargs)

    def init(self, **kwargs):
        """
        Use this call to arrange Pickup or Dropoff. Should call shopee.logistics.GetParameterForInit to fetch all required param first.
        pickup = {}
        dropoff = {}
        non_integrated = {}
        :param kwargs:
        :return:
        """
        return self.client.execute("logistics/init", "POST", kwargs)

    def set_logistic_status(self, **kwargs):
        """
        Set Logistic Status to PICKUP_DONE, this API only works for non-integrated logistic channels

        :param kwargs:
        :return:
        """
        return self.client.execute("logistics/init", "POST", kwargs)

    def set_tracking_no(self, **kwargs):
        """
        User this call to set tracking number for each order in batch.
        One order can only have one tracking number.
        This API can only be used on orders with the logisitcs channels that need sellers to provide tracking no to Shopee,
        instead that tracking no is generated from Shopee.
        :param kwargs:
        :return:
        """
        return self.client.execute("logistics/tracking_number/set_mass", "POST", kwargs)

    def get_logistic_info(self, **kwargs):
        """
        Get all the logistics info of an order to Init. 
        This API consolidates the output of GetParameterForInit, GetAddresss, GetTimeSlot and GetBranch 
        based on each order so that developer can get all the required parameters ready in this API for Init.

        This API is an alternative of GetParameterForInit, GetAddresss, GetTimeSlot and GetBranch as a set.
        
        @@Significant OpenAPI Updates (2018-09-15/2018-09-11)
        [optional new flow added in Documentation]
         - alternative for get_parameter_for_init (GetParameterForInit)
         - alternative for get_address (GetAddress)
         - alternative for get_time_slot (GetTimeSlot)
         - alternative for get_branch (GetBranch)
        """

        return self.client.execute("logistics/init_info/get", "POST", kwargs)












