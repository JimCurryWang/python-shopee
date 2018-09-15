from .base import BaseModule


class Discount(BaseModule):
    '''@@Significant OpenAPI Updates (2018-09-15/2018-??-??)
    '''

    def add_discount(self, **kwargs):
        """
        Use this api to add shop discount activity

        :param:
        :return:

        """
        return self.client.execute("discount/add", "POST", kwargs)

    def add_discount_item(self, **kwargs):
        """
        Use this api to add shop discount item
        :param:
        :return:
        
        """
        return self.client.execute("discount/items/add", "POST", kwargs)

    def delete_discount(self, **kwargs):
        """
        Use this api to delete one discount activity
        :param:
        :return:
        
        """
        return self.client.execute("discount/delete", "POST", kwargs)

    def delete_discount_item(self, **kwargs):
        """
        Use this api to delete items of the discount activity
        :param:
        :return:
        
        """
        return self.client.execute("discount/item/delete", "POST", kwargs)

    def get_discount_detail(self, **kwargs):
        """
        Use this api to get one shop discount activity detail
        :param:
        :return:
        
        """
        return self.client.execute("discount/detail", "POST", kwargs)

    def get_discounts_list(self, **kwargs):
        """
        Use this api to get shop discount activity list
        :param:
        :return:
        
        """
        return self.client.execute("discounts/get", "POST", kwargs)

    def update_discount(self, **kwargs):
        """
        Use this api to update one discount information
        :param:
        :return:
        
        """
        return self.client.execute("discount/update", "POST", kwargs)

    def update_discount_items(self, **kwargs):
        """
        Use this api to update items of the discount activity
        :param:
        :return:
        
        """
        return self.client.execute("discount/items/update", "POST", kwargs)




