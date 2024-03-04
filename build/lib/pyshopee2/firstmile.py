from .base import BaseModule


class FirstMile(BaseModule):

    def get_unbind_order_list(self, **kwargs):
        """
        Use this api to get unbind order list.
.
        :param kwargs:
         - cursor
         - page_size
         - response_optional_fields

        """
        return self.client.execute("first_mile/get_unbind_order_list", "GET", kwargs)

    def get_detail(self, **kwargs):
        """
        Use this api to get first mile detail.
.
        :param kwargs:
         - first_mile_tracking_number Required
         - cursor
        """
        return self.client.execute("first_mile/get_detail", "GET", kwargs)

    def generate_first_mile_tracking_number(self, **kwargs):
        """
        Use this api to generate first mile tracking number

        :param kwargs:
         - declare_date Required
         - quantity
         - seller_info Required
            - address Required
            - name Required
            - zipcode Required
            - region Required
            - phone Required
        """
        return self.client.execute("first_mile/generate_first_mile_tracking_number", "POST", kwargs)

    def bind_first_mile_tracking_number(self, **kwargs):
        """
        Use this api to bind first mile tracking number.

        :param kwargs:
        - first_mile_tracking_number Required
        - shipment_method Required
        - region Required
        - logistics_channel_id Required
        - volume
        - weight
        - width
        - length
        - height
        - order_list Required
            - order_sn Required
            - package_number
        """
        return self.client.execute("first_mile/bind_first_mile_tracking_number", "POST", kwargs)

    def unbind_first_mile_tracking_number(self, **kwargs):
        """
        Use this api to unbind first mile.

        :param kwargs:
        - first_mile_tracking_number Required
        - order_list Required
            - order_sn Required
            - package_number
        """
        return self.client.execute("first_mile/unbind_first_mile_tracking_number", "POST", kwargs)

    def get_tracking_number_list(self, **kwargs):
        """
        Use this api to get first mile tracking number list.

        :param kwargs:
        - from_date Required
        - to_date Required
        - page_size
        - cursor
        """
        return self.client.execute("first_mile/get_tracking_number_list", "GET", kwargs)

    def get_waybill(self, **kwargs):
        """
        Use this api to get first mile waybill file.

        :param kwargs:
        - first_mile_tracking_number_list Required
        """
        return self.client.execute("first_mile/get_waybill", "GET", kwargs)

    def get_channel_list(self, **kwargs):
        """
        Use this api to update items of the discount activity

        :param kwargs:
        - region Required

        """
        return self.client.execute("first_mile/get_channel_list", "GET", kwargs)
