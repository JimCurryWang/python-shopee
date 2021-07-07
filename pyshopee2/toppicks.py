from .base import BaseModule

class Toppicks(BaseModule):

    def get_top_picks_list(self, **kwargs):
        """
        get one TopPicks
.
        :param kwargs:
        """
        return self.client.execute("top_picks/get_top_picks_list", "GET", kwargs)


    def add_top_picks(self, **kwargs):
        """
        add one collection
.
        :param kwargs:
         - name (Required)
         - item_id_list (Required)
         - is_activated (Required)
        """
        return self.client.execute("top_picks/add_top_picks", "POST", kwargs)


    def update_top_picks(self, **kwargs):
        """
        update a collection info

        :param kwargs:
         - top_picks_id  (Required)
         - name
         - item_id_list
         - is_activated
        """
        return self.client.execute("top_picks/update_top_picks", "POST", kwargs)


    def delete_top_picks(self, **kwargs):
        """
        Delete a collection.
        :param kwargs:
        - top_picks_id  (Required)
        """
        return self.client.execute("top_picks/delete_top_picks", "POST", kwargs)
