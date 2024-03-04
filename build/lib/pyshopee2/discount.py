from .base import BaseModule


class Discount(BaseModule):

    def add_discount(self, **kwargs):
        """
        Use this api to add shop discount activity
.
        :param kwargs:
         - discount_name Required
         - start_time Required
         - end_time Required

        """
        return self.client.execute("discount/add_discount", "POST", kwargs)

    def add_discount_item(self, **kwargs):
        """
        Use this api to add shop discount item
.
        :param kwargs:
         - discount_id Required
         - item_list Required
            - item_id Required
            - model_list
                - model_id Required
                - model_promotion_price Required
                - model_promotion_stock
            - item_promotion_price
            - purchase_limit Required
            - item_promotion_stock

        """
        return self.client.execute("discount/add_discount_item", "POST", kwargs)

    def delete_discount(self, **kwargs):
        """
        Use this api to delete one discount activity

        :param kwargs:
         - discount_id Required
        """
        return self.client.execute("discount/delete_discount", "POST", kwargs)

    def delete_discount_item(self, **kwargs):
        """
        Use this api to delete items of the discount activity

        :param kwargs:
        - discount_id Required
        - item_id Required
        - model_id
        """
        return self.client.execute("discount/delete_discount_item", "POST", kwargs)

    def get_discount(self, **kwargs):
        """
        Use this api to get one shop discount activity detail

        :param kwargs:
        - discount_id Required
        - page_no Required
        - page_size Required
        """
        return self.client.execute("discount/get_discount", "GET", kwargs)

    def get_discount_list(self, **kwargs):
        """
        Use this api to get shop discount activity list

        :param kwargs:
        - discount_status Required
        - page_no Required
        - page_size Required
        """
        return self.client.execute("discount/get_discount_list", "GET", kwargs)

    def update_discount(self, **kwargs):
        """
        Use this api to update one discount information

        :param kwargs:
        - discount_id Required
        - discount_name
        - end_time
        - start_time
        """
        return self.client.execute("discount/update_discount", "POST", kwargs)

    def update_discount_item(self, **kwargs):
        """
        Use this api to update items of the discount activity

        :param kwargs:
        - discount_id Required
        - item_list Required
            - item_id Required
            - model_list
                - model_id Required
                - model_promotion_price Required
            - item_promotion_price
            - purchase_limit
        """
        return self.client.execute("discount/update_discount_item", "POST", kwargs)

    def end_discount(self, **kwargs):
        """
        Use this api to end shop discount activity

        :param kwargs:
        - discount_id

        """
        return self.client.execute("discount/end_discount", "POST", kwargs)

