from .base import BaseModule


class FollowPrize(BaseModule):

    def add_follow_prize(self, **kwargs):
        """
        OpenAPI add Follow Prize
.
        :param kwargs:

        """
        return self.client.execute("voucher/add_follow_prize", "POST", kwargs)

    def delete_follow_prize(self, **kwargs):
        """
        delete_follow_prize
.
        :param kwargs:

        """
        return self.client.execute("voucher/delete_follow_prize", "POST", kwargs)

    def end_follow_prize(self, **kwargs):
        """
        End follow prize

        :param kwargs:

        """
        return self.client.execute("voucher/end_follow_prize", "POST", kwargs)

    def update_follow_prize(self, **kwargs):
        """
        update_follow_prize

        :param kwargs:

        """
        return self.client.execute("voucher/update_follow_prize", "POST", kwargs)

    def get_follow_prize_detail(self, **kwargs):
        """
        get_follow_prize_detail

        :param kwargs:

        """
        return self.client.execute("voucher/get_follow_prize_detail", "GET", kwargs)

    def get_follow_prize_list(self, **kwargs):
        """
        get_follow_prize_list.

        :param kwargs:
        """
        return self.client.execute("voucher/get_follow_prize_list", "GET", kwargs)
