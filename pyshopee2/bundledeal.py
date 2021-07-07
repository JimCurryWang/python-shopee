from .base import BaseModule

class BundleDeal(BaseModule):

    def add_bundle_deal(self, **kwargs):
        """
        create bundle deal
.
        :param kwargs:
	    - rule_type Required
    	- discount_value Required
    	- fix_price Required
    	- discount_percentage Required
    	- min_amount Required
	    - start_time Required
	    - end_time Required
    	- name Required
    	- purchase_limit Required
        """
        return self.client.execute("bundle_deal/add_bundle_deal", "POST", kwargs)


    def add_bundle_deal_item(self, **kwargs):
        """
        add product to bundle deal
.
        :param kwargs:
         - bundle_deal_id Required
         - item_list Required
            - item_id Required
            - status Required
        """
        return self.client.execute("bundle_deal/add_bundle_deal_item", "POST", kwargs)


    def get_bundle_deal_list(self, **kwargs):
        """
        get bundle deal list

        :param kwargs:
         - page_size
         - time_status
         - page_no

        """
        return self.client.execute("bundle_deal/get_bundle_deal_list", "GET", kwargs)


    def get_bundle_deal(self, **kwargs):
        """
        get bundle deal detail

        :param kwargs:
        - bundle_deal_id Required
        """
        return self.client.execute("bundle_deal/get_bundle_deal", "GET", kwargs)

    def get_bundle_deal_item(self, **kwargs):
        """
        get bundle deal item

        :param kwargs:
        - bundle_deal_id Required

        """
        return self.client.execute("bundle_deal/get_bundle_deal_item", "GET", kwargs)

    def update_bundle_deal(self, **kwargs):
        """
        update bundle deal

        :param kwargs:
		- rule_type
		- discount_value
		- fix_price
		- discount_percentage
		- min_amount
		- start_time
		- end_time
		- name
		- purchase_limit
		- bundle_deal_id Required
        """
        return self.client.execute("bundle_deal/update_bundle_deal", "POST", kwargs)

    def update_bundle_deal_item(self, **kwargs):
        """
        update product in bundle deal

        :param kwargs:
        - bundle_deal_id Required
        - item_list Required
            - item_id Required
            - status Required
        """
        return self.client.execute("bundle_deal/update_bundle_deal_item", "POSt", kwargs)

    def end_bundle_deal(self, **kwargs):
        """
        end bundle deal

        :param kwargs:
        - bundle_deal_id Required

        """
        return self.client.execute("bundle_deal/end_bundle_deal", "POST", kwargs)

    def delete_bundle_deal(self, **kwargs):
        """
        delete bundle deal

        :param kwargs:
        - bundle_deal_id Required

        """
        return self.client.execute("bundle_deal/delete_bundle_deal", "POST", kwargs)

    def delete_bundle_deal_item(self, **kwargs):
        """
        delete product in bundle deal

        :param kwargs:
        - bundle_deal_id Required
        - item_list Required
            -item_id Required

        """
        return self.client.execute("bundle_deal/delete_bundle_deal_item", "POST", kwargs)
