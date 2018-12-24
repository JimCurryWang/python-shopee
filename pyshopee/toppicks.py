from .base import BaseModule

class Toppicks(BaseModule):

    def get_top_picks_list(self, **kwargs):
        """
        Get the list of all collections.
        :param kwargs:
        """
        return self.client.execute("top_picks/get", "POST", kwargs)


    def add_top_picks(self, **kwargs):
        """
        Add one collection. One shop can have up to 10 collections.
        :param kwargs:
        """
        return self.client.execute("top_picks/add", "POST", kwargs)


    def update_top_picks(self, **kwargs):
        """
        Use this API to update the collection name, the item list in a collection, or to activate a collection.
        :param kwargs:
        """
        return self.client.execute("top_picks/update", "POST", kwargs)


    def add_top_picks(self, **kwargs):
        """
        Delete a collection.
        :param kwargs:
        """
        return self.client.execute("top_picks/delete", "POST", kwargs)
