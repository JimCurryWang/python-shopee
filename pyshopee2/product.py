from .base import BaseModule


class Product(BaseModule):

    def get_comment(self, **kwargs):
        """
        Use this api to get comment by shop_id, item_id, or comment_id.
.
        :param kwargs:
         - item_id
         - comment_id
         - cursor Required
         - page_size Required
        """
        return self.client.execute("product/get_comment", "GET", kwargs)

    def reply_comment(self, **kwargs):
        """
        Use this api to reply comments from buyers in batch.
.
        :param kwargs:
         - comment_list Required
            - comment_id Required
            - comment Required
        """
        return self.client.execute("product/reply_comment", "POST", kwargs)

    def get_item_base_info(self, **kwargs):
        """
        Get the installment state of shop.

        :param kwargs:
        - item_id_list Required

        """
        return self.client.execute("product/get_item_base_info", "GET", kwargs)

    def get_item_extra_info(self, **kwargs):
        """
        Use this api to get extra info of item by item_id list.

        :param kwargs:
        - item_id_list Required

        """
        return self.client.execute("product/get_item_extra_info", "GET", kwargs)

    def get_item_list(self, **kwargs):
        """
        Use this call to get a list of items.

        :param kwargs:
        - offset Required
        - page_size Required
        - update_time_from
        - update_time_to
        - item_status Required
        """
        return self.client.execute("product/get_item_list", "GET", kwargs)

    def delete_item(self, **kwargs):
        """
        Use this call to delete a product item.

        :param kwargs:
        - item_id Required
        """
        return self.client.execute("product/delete_item", "POST", kwargs)

    def add_item(self, **kwargs):
        """
        Add a new item.

        :param kwargs:
        - original_price Required
        - description Required
        - weight
        - item_name Required
        - item_status
        - dimension
        - normal_stock Required
        - logistic_info Required
        - attribute_list
        - category_id Required
        - image Required
        - pre_order
        - item_sku
        - condition
        - wholesale
        - video_upload_id
        - brand
        - item_dangerous
        """
        return self.client.execute("product/add_item", "POST", kwargs)

    def update_item(self, **kwargs):
        """
        Update item.

        :param kwargs:

        """
        return self.client.execute("product/update_item", "POST", kwargs)

    def get_model_list(self, **kwargs):
        """
        Get model list of an item.

        :param kwargs:
        - item_id Required

        """
        return self.client.execute("product/get_model_list", "GET", kwargs)

    def update_size_chart(self, **kwargs):
        """
        Update size chart image of item.

        :param kwargs:
        - item_id Required
        - size_chart Required

        """
        return self.client.execute("product/update_size_chart", "POST", kwargs)

    def unlist_item(self, **kwargs):
        """
        Unlist item.

        :param kwargs:
        - item_list Required
            - item_id Required
            - unlist Required

        """
        return self.client.execute("product/unlist_item", "POST", kwargs)

    def boost_item(self, **kwargs):
        """
        Boost item.

        :param kwargs:
        - item_id_list Required

        """
        return self.client.execute("product/boost_item", "POST", kwargs)

    def get_boosted_list(self, **kwargs):
        """
        Get boosted item list.

        :param kwargs:
        - item_id Required

        """
        return self.client.execute("product/get_boosted_list", "GET", kwargs)

    def get_dts_limit(self, **kwargs):
        """
        Get day to shipping limit.

        :param kwargs:
        - category_id Required

        """
        return self.client.execute("product/get_dts_limit", "GET", kwargs)

    def get_item_limit(self, **kwargs):
        """
        Get item upload control.

        :param kwargs:
        - item_id Required

        """
        return self.client.execute("product/get_item_limit", "GET", kwargs)

    def support_size_chart(self, **kwargs):
        """
        Get category support size chart.

        :param kwargs:
        - category Required

        """
        return self.client.execute("product/support_size_chart", "GET", kwargs)


    def init_tier_variation(self, **kwargs):
        """
        Init item tier-variation struct.

        :param kwargs:
        - item_id Required
        - tier_variation Required
        - model Required

        """
        return self.client.execute("product/init_tier_variation", "POST", kwargs)

    def update_tier_variation(self, **kwargs):
        """
        Get category support size chart.

        :param kwargs:
        - item_id Required
        - tier_variation Required

        """
        return self.client.execute("product/update_tier_variation", "POST", kwargs)

    def update_model(self, **kwargs):
        """
        Update seller sku for model.

        :param kwargs:
        - item_id Required
        - model Required

        """
        return self.client.execute("product/update_model", "POST", kwargs)

    def add_model(self, **kwargs):
        """
        Add model.

        :param kwargs:
        - item_id Required
        - model_list Required

        """
        return self.client.execute("product/add_model", "POST", kwargs)

    def delete_model(self, **kwargs):
        """
        Delete item model.

        :param kwargs:
        - item_id Required
        - model_id Required

        """
        return self.client.execute("product/delete_model", "POST", kwargs)

    def update_price(self, **kwargs):
        """
        Update price.

        :param kwargs:
        - item_id Required
        - price_list Required
            - model_id
            - original_price Required
        """
        return self.client.execute("product/update_price", "POST", kwargs)

    def update_stock(self, **kwargs):
        """
        Update stock.

        :param kwargs:
        - item_id Required
        - stock_list Required
            - model_id
            - normal_stock Requested

        """
        return self.client.execute("product/update_stock", "POST", kwargs)

    def get_attributes(self, **kwargs):
        """
        Get attributes.

        :param kwargs:
        - language
        - category_id Required

        """
        return self.client.execute("product/get_attributes", "GET", kwargs)

    def get_category(self, **kwargs):
        """
        Get category..

        :param kwargs:
        - language

        """
        return self.client.execute("product/get_category", "GET", kwargs)

    def get_item_promotion(self, **kwargs):
        """
        Get item promotion info.

        :param kwargs:
        - item_id_list Required

        """
        return self.client.execute("product/get_item_promotion", "GET", kwargs)

    def update_sip_item_price(self, **kwargs):
        """
        Update sip item price.

        :param kwargs:
        - item_id Required
        - sip_item_price
            - model_id
            - sip_item_price

        """
        return self.client.execute("product/update_sip_item_price", "POST", kwargs)

    def get_brand_list(self, **kwargs):
        """
        Use this call to get a list of brand.

        :param kwargs:
        - offset
        - page_size Required
        - category_id Required
        - status Required

        """
        return self.client.execute("product/get_brand_list", "GET", kwargs)

    def search_item(self, **kwargs):
        """
        Use this call to search item.

        :param kwargs:
        - offset
        - page_size Required
        - item_name
        - attribute_status

        """
        return self.client.execute("product/search_item", "GET", kwargs)

    def category_recommend(self, **kwargs):
        """
        Recommend category by item name.

        :param kwargs:
        - item_name Required

        """
        return self.client.execute("product/category_recommend", "GET", kwargs)

