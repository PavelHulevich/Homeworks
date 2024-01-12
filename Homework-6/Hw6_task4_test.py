import unittest
from Hw6_task4 import find_max_items_entrance


class TestFunction(unittest.TestCase):
    def test1(self):
        self.assertEqual(find_max_items_entrance([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [3,6,9])
    def test11(self):
        self.assertEqual(find_max_items_entrance([[1, 25, 3], [11, 5, 6], [9.65, 8, 9]]), [25, 11, 9.65])
    def test2(self):
        self.assertEqual(find_max_items_entrance([[1, 2, 3], [4, 5], [7, '8', 9]]), 101)
    def test3(self):
        self.assertEqual(find_max_items_entrance([[1, 2, '3'], [4, 5, 6], [7, 8, 9]]), 101)
    def test4(self):
        self.assertEqual(find_max_items_entrance(55), 100)
    def test41(self):
        self.assertEqual(find_max_items_entrance('55'), 100)
    def test5(self):
        self.assertEqual(find_max_items_entrance([[1, 2, 3], 85, [7, 8, 9]]), 102)
    def test6(self):
        self.assertEqual(find_max_items_entrance([[1, 2, 3], 'ss', [7, 8, 9]]), 102)

