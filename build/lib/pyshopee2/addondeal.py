from .base import BaseModule


class AddonDeal(BaseModule):

    def add_add_on_deal(self, **kwargs):
        """
        Add Add-on Deal
.
        :param kwargs:
         - add_on_deal_name Required
         - start_time Required
         - end_time Required
         - promotion_type Required
         - purchase_min_spend
         - per_gift_num
         - promotion_purchase_limit
        """
        return self.client.execute("add_on_deal/add_add_on_deal", "POST", kwargs)


    def add_add_on_deal_main_item(self, **kwargs):
        """
        Add Add-on Deal Main Item
.
        :param kwargs:
         - add_on_deal_id Required
         - main_item_list Required
            - item_id Required
            - status Required
        """
        return self.client.execute("add_on_deal/add_add_on_deal_main_item", "POST", kwargs)


    def add_add_on_deal_sub_item(self, **kwargs):
        """
        Add Add-on Deal Sub Item

        :param kwargs:
         - add_on_deal_id Required
         - sub_item_list Required
            - item_id
            - model_id
            - status
            - sub_item_input_price
            - sub_item_limit
        """
        return self.client.execute("add_on_deal/add_add_on_deal_sub_item", "POST", kwargs)


    def delete_add_on_deal(self, **kwargs):
        """
        Delete Add-on Deal

        :param kwargs:
        - add_on_deal_id Required
        """
        return self.client.execute("add_on_deal/delete_add_on_deal", "POST", kwargs)

    def delete_add_on_deal_main_item(self, **kwargs):
        """
        Delete Add-on Deal Main Item

        :param kwargs:
        - add_on_deal_id Required
        - main_item_list Required
        """
        return self.client.execute("add_on_deal/delete_add_on_deal_main_item", "POST", kwargs)

    def delete_add_on_deal_sub_item(self, **kwargs):
        """
        Delete Add-on Deal Sub Item

        :param kwargs:
        - add_on_deal_id Required
        - sub_item_list Required
            - item_id
            - model_id
        """
        return self.client.execute("add_on_deal/delete_add_on_deal_sub_item", "POST", kwargs)

    def get_add_on_deal_list(self, **kwargs):
        """
        Get Add-on Deal List

        :param kwargs:
        - promotion_status Required
        - page_no
        - page_size
        """
        return self.client.execute("add_on_deal/get_add_on_deal_list", "GET", kwargs)

    def get_add_on_deal(self, **kwargs):
        """
        Get Add-on Deal

        :param kwargs:
        - add_on_deal_id Required

        """
        return self.client.execute("add_on_deal/get_add_on_deal", "GET", kwargs)

    def get_add_on_deal_main_item(self, **kwargs):
        """
        Get Add-on Deal Main Item

        :param kwargs:
        - add_on_deal_id Required

        """
        return self.client.execute("add_on_deal/get_add_on_deal_main_item", "GET", kwargs)

    def get_add_on_deal_sub_item(self, **kwargs):
        """
        Get Add-on Deal Sub Item

        :param kwargs:
        - add_on_deal_id Required

        """
        return self.client.execute("add_on_deal/get_add_on_deal_sub_item", "GET", kwargs)

    def update_add_on_deal(self, **kwargs):
        """
        Update Add-on Deal

        :param kwargs:
        - add_on_deal_id Required
        - start_time
        - end_time
        - purchase_min_spend
        - per_gift_num
        - promotion_purchase_limit
        - sub_item_priority
        - add_on_deal_name
        """
        return self.client.execute("add_on_deal/update_add_on_deal", "POST", kwargs)

    def update_add_on_deal_main_item(self, **kwargs):
        """
        Update Add-on Deal Main Item

        :param kwargs:
        - add_on_deal_id Required
        - main_item_list Required
            - item_id Required
            - status Required
        """
        return self.client.execute("add_on_deal/update_add_on_deal_main_item", "POST", kwargs)

    def update_add_on_deal_sub_item(self, **kwargs):
        """
        Update Add-on Deal Sub Item

        :param kwargs:
        - add_on_deal_id Required
        - sub_item_list Required
            - item_id
            - model_id
            - status
            - sub_item_input_price
            - sub_item_limit
        """
        return self.client.execute("add_on_deal/update_add_on_deal_sub_item", "POST", kwargs)

    def end_add_on_deal(self, **kwargs):
        """
        End Add-on Deal

        :param kwargs:
        - add_on_deal_id Required

        """
        return self.client.execute("add_on_deal/end_add_on_deal", "POST", kwargs)