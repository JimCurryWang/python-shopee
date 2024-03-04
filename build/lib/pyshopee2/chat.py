from .base import BaseModule


class Chat(BaseModule):
    def get_message(self, **kwargs):
        """
            To get messages history for a specific conversation, which can display the messages detail from sender and receiver.

        :param kwargs
            - offset
            - page_size
            - conversation_id (Required)
        :return
        https://open.shopee.com/documents?module=109&type=1&id=671&version=2
        """
        return self.client.execute("sellerchat/get_message", "GET", kwargs)

    def send_message(self, **kwargs):
        """
            1.To send a message and select the correct message type (Do not use this API to send batch messages) 2.Currently TW region is not supported to send messages.

        :param kwargs
            - to_id (Required)
            - message_type  (Required)
            - content  (Required)
                - text
                - sticker_id
                - sticker_package_id
                - image_url
                - item_id
                - order_sn
        :return
        https://open.shopee.com/documents?module=109&type=1&id=672&version=2
        """
        return self.client.execute("sellerchat/send_message", "POST", kwargs)

    def get_conversation_list(self, **kwargs):
        """
            To get conversation list and its params data


        :param kwargs
            - direction (Required)
            - type (Required)
            - next_timestamp_nano
            - page_size
        :return
        https://open.shopee.com/documents?module=109&type=1&id=673&version=2
        """
        return self.client.execute("sellerchat/get_conversation_list", "GET", kwargs)

    def get_one_conversation(self, **kwargs):
        """
            To get a specific conversation's basic information.


        :param kwargs
            - conversation_id  (Required)

        :return
        https://open.shopee.com/documents?module=109&type=1&id=674&version=2
        """
        return self.client.execute("sellerchat/get_one_conversation", "GET", kwargs)

    def delete_conversation(self, **kwargs):
        """
            To delete a specific conversation

        :param kwargs
            - conversation_id  (Required)

        :return
        https://open.shopee.com/documents?module=109&type=1&id=675&version=2
        """
        return self.client.execute("sellerchat/delete_conversation", "POST", kwargs)

    def get_unread_conversation_count(self, **kwargs):
        """
            To get the number of unread conversations from a shop (not unread messages)
        :param kwargs
        :return
        https://open.shopee.com/documents?module=109&type=1&id=676&version=2
        """

        return self.client.execute("sellerchat/get_unread_conversation_count", "GET", kwargs)

    def pin_conversation(self, **kwargs):
        """
            To pin a specific conversations

        :param kwargs
            - conversation_id  (Required)

        :return
        https://open.shopee.com/documents?module=109&type=1&id=677&version=2
        """
        return self.client.execute("sellerchat/pin_conversation", "POST", kwargs)

    def unpin_conversation(self, **kwargs):
        """
            To unpin a specific conversations

        :param kwargs
            - conversation_id  (Required)

        :return
        https://open.shopee.com/documents?module=109&type=1&id=678&version=2
        """
        return self.client.execute("sellerchat/unpin_conversation", "POST", kwargs)

    def read_conversation(self, **kwargs):
        """
            To send read request for a specific conversation

        :param kwargs
            - conversation_id  (Required)
            - last_read_message_id (Required)

        :return
        https://open.shopee.com/documents?module=109&type=1&id=679&version=2
        """
        return self.client.execute("sellerchat/read_conversation", "POST", kwargs)

    def unread_conversation(self, **kwargs):
        """
            To mark a conversation as unread

        :param kwargs
            - conversation_id  (Required)

        :return
        https://open.shopee.com/documents?module=109&type=1&id=680&version=2
        """
        return self.client.execute("sellerchat/unread_conversation", "POST", kwargs)

    def get_offer_toggle_status(self, **kwargs):
        """
            To get the toggle status to check if the shop has allowed buyer to negotiate price with seller.

        :param kwargs
        :return
        https://open.shopee.com/documents?module=109&type=1&id=681&version=2
        """
        return self.client.execute("sellerchat/get_offer_toggle_status", "GET", kwargs)

    def set_offer_toggle_status(self, **kwargs):
        """
            To set the toggle status.If set as "enabled", then seller doesn't allow buyer negotiate the price.


        :param kwargs
            - make_offer_status (Required)

        :return
        https://open.shopee.com/documents?module=109&type=1&id=682&version=2
        """
        return self.client.execute("sellerchat/set_offer_toggle_status", "POST", kwargs)

    def upload_image(self, **kwargs):
        """
            When you need to send an image type message, please request this API first to upload the image file to get image url. Then proceed to request the send message API with the image url.

        :param kwargs
            - file (Required)

        :return
        https://open.shopee.com/documents?module=109&type=1&id=682&version=2
        """
        return self.client.execute("sellerchat/upload_image", "POST", kwargs)
