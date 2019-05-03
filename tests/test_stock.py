import unittest

import stocksim


class StockTestCase(unittest.TestCase):

    def test_serialize(self):
        stock = stocksim.stock.Stock(
            ticker='FOO', price=100.0, count=5, history=[]
        )
        self.assertEqual(
            stocksim.stock.serialize(stock),
            {'ticker': 'FOO', 'price': 100.0, 'count': 5, 'history': []}
        )
