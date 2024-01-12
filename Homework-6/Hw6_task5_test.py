import unittest
from Hw6_task5 import transpose_2dim_list_entrance


class TestFunction(unittest.TestCase):
    def test1(self):
        self.assertEqual(transpose_2dim_list_entrance([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[1, 4, 7], [2, 5, 8], [3, 6, 9]])
    def test11(self):
        self.assertEqual(transpose_2dim_list_entrance([[1, 2, 3], [4, 5, 6], [7.65, 8, 9]]), [[1, 4, 7.65], [2, 5, 8], [3, 6, 9]])
    def test2(self):
        self.assertEqual(transpose_2dim_list_entrance([[1, 2, 3], [4, 5, ], [7, 8, 9]]), 0b0100)
    def test3(self):
        self.assertEqual(transpose_2dim_list_entrance([[1, 2, '3'], [4, 5, 6], [7, 8, 9]]), 0b1000)
    def test4(self):
        self.assertEqual(transpose_2dim_list_entrance(55), 0b0001)
    def test41(self):
        self.assertEqual(transpose_2dim_list_entrance('55'), 0b0001)
    def test5(self):
        self.assertEqual(transpose_2dim_list_entrance([[1, 2, 3], 85, [7, 8, 9]]), 0b0010)
    def test6(self):
        self.assertEqual(transpose_2dim_list_entrance([[1, 2, 3], [7, 8, 9]]), 0b0100)

