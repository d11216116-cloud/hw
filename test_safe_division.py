import unittest
from your_module import safe_division  # 根據實際模組名稱調整


class TestSafeDivision(unittest.TestCase):
    """safe_division 函數的單元測試"""

    def test_normal_division(self):
        """測試正常的除法運算"""
        self.assertEqual(safe_division(10, 2), 5)
        self.assertEqual(safe_division(15, 3), 5)
        self.assertEqual(safe_division(7, 2), 3.5)

    def test_division_with_negative_numbers(self):
        """測試負數的除法"""
        self.assertEqual(safe_division(-10, 2), -5)
        self.assertEqual(safe_division(10, -2), -5)
        self.assertEqual(safe_division(-10, -2), 5)

    def test_division_by_zero(self):
        """測試除以零的錯誤處理"""
        result = safe_division(10, 0)
        self.assertEqual(result, "錯誤：除數不能為零！")

    def test_division_by_zero_with_zero_numerator(self):
        """測試分子為零且除數為零"""
        result = safe_division(0, 0)
        self.assertEqual(result, "錯誤：除數不能為零！")

    def test_division_with_floats(self):
        """測試浮點數的除法"""
        self.assertAlmostEqual(safe_division(10.5, 2.5), 4.2, places=5)
        self.assertAlmostEqual(safe_division(1.0, 3.0), 0.333333, places=5)

    def test_division_of_zero(self):
        """測試分子為零的情況"""
        self.assertEqual(safe_division(0, 5), 0)
        self.assertEqual(safe_division(0, -5), 0)

    def test_large_numbers(self):
        """測試大數字的除法"""
        self.assertEqual(safe_division(1000000, 1000), 1000)
        self.assertEqual(safe_division(999999, 3), 333333)


if __name__ == '__main__':
    unittest.main()
