# /usr/bin/env python
# -*- coding:utf8 -*-
from unittest import TestCase
import shopee

class TestClient(TestCase):
    def test_shopee_client(self):
        client = shopee.Client(24234, 23423, "23432432")
        self.assertEqual(client.shop_id, "18787076")
