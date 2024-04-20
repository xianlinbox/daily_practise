import unittest
from solution import Solution


class TestJump(unittest.TestCase):
    solution = Solution()

    def test_case_0(self):
        result = self.solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
        self.assertEqual(49, result)

    def test_case_1(self):
        result = self.solution.maxArea([1, 8, 8, 2, 2])
        self.assertEqual(8, result)

    def test_case_2(self):
        result = self.solution.maxArea([1, 1])
        self.assertEqual(1, result)


if __name__ == "__main__":
    unittest.main()
