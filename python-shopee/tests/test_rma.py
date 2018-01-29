# /usr/bin/env python
# -*- coding:utf8 -*-
from unittest import TestCase
import shopee


class TestRMA(TestCase):

    def test_shopee_get_return_list(self):
        client = shopee.Client(234243, 23432, "23423")
        # resp = client.order.query(create_time_from = 1512117303, create_time_to=1512635703)
        # if resp.status_code == 200:
        #     print(resp.text)
        resp = client.rma.get_return_list()
        print(resp.text)
        # 171207162767U5V

