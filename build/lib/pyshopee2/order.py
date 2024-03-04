from .base import BaseModule


class Order(BaseModule):

    def get_order_list(self, **kwargs):
        """
        Use this api to search orders.

        :param kwargs:
         - time_range_field Required
         - time_from Required
         - time_to Required
         - page_size Required
         - cursor
         - order_status
         - response_optional_fields

        """
        return self.client.execute("order/get_order_list", "GET", kwargs)

    def get_shipment_list(self, **kwargs):
        """
        Use this api to get order list which order_status is READY_TO_SHIP.

        :param kwargs:
         - cursor
         - page_size Required

        """
        return self.client.execute("order/get_shipment_list", "GET", kwargs)

    def get_order_detail(self, **kwargs):
        """
        Use this api to get order detail.

        :param kwargs:
         - order_sn_list Required
         - response_optional_fields
        """
        return self.client.execute("order/get_order_detail", "GET", kwargs)

    def split_order(self, **kwargs):
        """
        Use this api to split an order into multiple packages.

        :param kwargs:
        - order_sn Required
        - package_list Required
        - item_list Required
            - item_id Required
            - model_id Required
            - order_item_id
            - promotion_group_id
        """
        return self.client.execute("order/split_order", "POST", kwargs)

    def unsplit_order(self, **kwargs):
        """
        Use this ai to undo split of order. After undo split, the order will have only one package.

        :param kwargs:
        - order_sn Required
        """
        return self.client.execute("order/unsplit_order", "POST", kwargs)

    def cancel_order(self, **kwargs):
        """
        Use this api to cancel an order

        :param kwargs:
        - order_sn Required
        - cancel_reason Required
        - item_list
            - item_id Required
            - model_id Required
        """
        return self.client.execute("order/cancel_order", "POST", kwargs)

    def handle_buyer_cancellation(self, **kwargs):
        """
        Use this api to handle buyer's cancellation application.

        :param kwargs:
        - order_sn Required
        - operation Required

        """
        return self.client.execute("order/handle_buyer_cancellation", "POST", kwargs)

    def set_note(self, **kwargs):
        """
        Use this api to set note for an order.

        :param kwargs:
        - order_sn Required
        - note Required
        """
        return self.client.execute("order/set_note", "POST", kwargs)

    def add_invoice_data(self, **kwargs):
        """
        Use the API to add invoice data of the order when the order status is PENDING_INVOICE under some special logistics channels, such as Total Express, only for the BR local seller.

        :param kwargs:
        - order_sn Required
        - invoice_data Required
            - number Required
            - series_number Required
            - access_key Required
            - issue_date Required
            - total_value Required
            - products_total_value Required
            - tax_code Required
        """
        return self.client.execute("order/add_invoice_data", "POST", kwargs)

