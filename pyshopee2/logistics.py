from .base import BaseModule


class Logistics(BaseModule):

    def get_shipping_parameter(self, **kwargs):
        """
        Use this api to get shipping parameter.
.
        :param kwargs:
        - order_sn Required
        """
        return self.client.execute("logistics/get_shipping_parameter", "GET", kwargs)

    def get_tracking_number(self, **kwargs):
        """
        Use this api to get tracking_number when you hava shipped order.
.
        :param kwargs:
         - order_sn Required
         - package_number
         - response_optional_fields
        """
        return self.client.execute("logistics/get_tracking_number", "GET", kwargs)

    def ship_order(self, **kwargs):
        """
        Use this api to initiate logistics including arrange pickup, dropoff or shipment for non-integrated logistic channels. Should call v2.logistics.get_shipping_parameter to fetch all required param first. It's recommended to initiate logistics one hour after the orders were placed since there is one-hour window buyer can cancel any order without request to seller.

        :param kwargs:
         - order_sn Required
         - package_number
         - pickup
            - address_id
            - pickup_time_id
            - tracking_number
        - dropoff
            - branch_id
            - sender_real_name
            - tracking_number
        - non_integrated
            - tracking_number

        """
        return self.client.execute("logistics/ship_order", "POST", kwargs)

    def update_shipping_order(self, **kwargs):
        """
        Use this api to update pickup address and pickup time for shipping order.

        :param kwargs:
         - order_sn Required
         - package_number
         - pickup
            - address_id Required
            - pickup_time_id Required

        """
        return self.client.execute("logistics/update_shipping_order", "POST", kwargs)

    def get_shipping_document_parameter(self, **kwargs):
        """
        Use this api to get the selectable shipping_document_type and suggested shipping_document_type.

        :param kwargs:
        - order_list Required
            - order_sn Required
            - package_number

        """
        return self.client.execute("logistics/get_shipping_document_parameter", "POST", kwargs)

    def create_shipping_document(self, **kwargs):
        """
        Use this api to create shipping document task for each order or package

        :param kwargs:
        - order_list Required
            - order_sn Required
            - package_number
            - tracking_number
            - shipping_document_type
        """
        return self.client.execute("logistics/create_shipping_document", "POST", kwargs)

    def get_shipping_document_result(self, **kwargs):
        """
        Use this api to get the shipping_document of each order or package status.

        :param kwargs:
        - order_list Required
            - order_sn Required
            - package_number
            - shipping_document_type

        """
        return self.client.execute("logistics/get_shipping_document_result", "POST", kwargs)

    def download_shipping_document(self, **kwargs):
        """
        Use this api to download shipping_document. You have to call v2.logistics.create_shipping_document to create a new shipping document task first and call v2.logistics.get_shipping_document_resut to get the task status second. If the task is READY, you can download this shipping document.

        :param kwargs:
        - shipping_document_type
        - order_list Required
            - order_sn Required
            - package_number
        """
        return self.client.execute("logistics/download_shipping_document", "POST", kwargs)

    def get_shipping_document_info(self, **kwargs):
        """
        Use this api to fetch the logistics information of an order, these info can be used for airwaybill printing. Dedicated for crossborder SLS order airwaybill.

        :param kwargs:
        - order_sn Required
        - package_number

        """
        return self.client.execute("logistics/get_shipping_document_info", "GET", kwargs)

    def get_tracking_info(self, **kwargs):
        """
        Use this api to get the logistics tracking information of an order.

        :param kwargs:
        - order_sn Required
        - package_number

        """
        return self.client.execute("logistics/get_tracking_info", "GET", kwargs)

    def get_address_list(self, **kwargs):
        """
        For integrated logistics channel, use this call to get pickup address for pickup mode order.

        :param kwargs:

        """
        return self.client.execute("logistics/get_address_list", "GET", kwargs)

    def set_address_config(self, **kwargs):
        """
        Use this API to set address config of your shop.

        :param kwargs:
        - show_pickup_address
        - address_type_config
            - address_id
            - address_type

        """
        return self.client.execute("logistics/set_address_config", "POST", kwargs)

    def delete_address(self, **kwargs):
        """
        Use this api to delete address

        :param kwargs:
        - address_id Required

        """
        return self.client.execute("logistics/delete_address", "POST", kwargs)

    def get_channel_list(self, **kwargs):
        """
        Use this api to get all supported logistic channels.

        :param kwargs:
        """
        return self.client.execute("logistics/get_channel_list", "GET", kwargs)

    def update_channel(self, **kwargs):
        """
        Use this api to update shop level logistics channel's configuration.

        :param kwargs:
        - logistics_channel_id Required
        - enabled
        - preferred
        - cod_enabled
        """
        return self.client.execute("logistics/update_channel", "POST", kwargs)

    def get_channel_list(self, **kwargs):
        """
        Use this api to get all supported logistic channels.

        :param kwargs:
        """
        return self.client.execute("logistics/get_channel_list", "GET", kwargs)

    def batch_ship_order(self, **kwargs):
        """
        Use this api to batch initiate logistics including arrange pickup, dropoff or shipment for non-integrated logistic channels. Should call v2.logistics.get_shipping_parameter to fetch all required param first. It's recommended to initiate logistics one hour after the orders were placed since there is one-hour window buyer can cancel any order without request to seller.

        :param kwargs:
        - order_list Required
            - order_sn Required
            - package_number
        - pickup
            - address_id
            - pickup_time_id
            - tracking_number
        - dropoff
            - branch_id
            - sender_real_name
            - tracking_number
        - non_integrated
            - non_integrated
        """
        return self.client.execute("logistics/batch_ship_order", "POST", kwargs)
