import unittest
from Hw6_task1 import find_max_common_multiplier


class TestFindMaxCommonItem(unittest.TestCase):
    def test_find_max_common_multiplier1(self):
        self.assertEqual(find_max_common_multiplier(21, 28), 7)

    def test_find_max_common_multiplier11(self):
        self.assertEqual(find_max_common_multiplier(35, 28), 7)

    def test_find_max_common_multiplier2(self):
        self.assertEqual(find_max_common_multiplier(-2, 7), 0)

    def test_find_max_common_multiplier3(self):
        self.assertEqual(find_max_common_multiplier(5, -4), 0)

    def test_find_max_common_multiplier4(self):
        self.assertEqual(find_max_common_multiplier(5, 0), 0)

    def test_find_max_common_multiplier5(self):
        self.assertEqual(find_max_common_multiplier(0, 88), 0)

    def test_find_max_common_multiplier6(self):
        self.assertEqual(find_max_common_multiplier(3.25, 44), 0)

    def test_find_max_common_multiplier7(self):
        self.assertEqual(find_max_common_multiplier(99, 4.75), 0)

    def test_find_max_common_multiplier8(self):
        self.assertEqual(find_max_common_multiplier('99', 4.75), 0)

    def test_find_max_common_multiplier9(self):
        self.assertEqual(find_max_common_multiplier(9, 7), 1)




