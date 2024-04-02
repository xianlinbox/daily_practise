import unittest
from stock import Solution


class TestStockStrategy(unittest.TestCase):
    solution = Solution()

    def test_case_1(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(7, self.solution.maxProfit(prices=prices))

    def test_case_2(self):
        prices = [1, 2, 3, 4, 5]
        self.assertEqual(4, self.solution.maxProfit(prices=prices))

    def test_case_3(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(0, self.Solution.maxProfit(prices=prices))


if __name__ == "__main__":
    unittest.main()
