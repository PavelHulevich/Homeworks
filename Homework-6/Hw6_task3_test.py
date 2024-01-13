import unittest
from Hw6_task3 import find_max_min_entrance


class TestFunction(unittest.TestCase):
    def test1(self):
        self.assertEqual(find_max_min_entrance([34, 87, 5.3, 475, 56, 765, 321]), True)
    def test11(self):
        self.assertEqual(find_max_min_entrance('sdsd'), False)
    def test2(self):
        self.assertEqual(find_max_min_entrance(23), False)
    def test3(self):
        self.assertEqual(find_max_min_entrance([1, [4, 5, 6], [7, 8, 9]]), False)
    def test4(self):
        self.assertEqual(find_max_min_entrance([34, 87, 5.3, 'sss', 56, 765, 321]), False)
    def test41(self):
        self.assertEqual(find_max_min_entrance('55'), False)
    def test5(self):
        self.assertEqual(find_max_min_entrance([[1, 2, 3], 85, [7, 8, 9]]), False)
    def test6(self):
        self.assertEqual(find_max_min_entrance([[1, 2, 3], [7, 8, 9]]), False)

