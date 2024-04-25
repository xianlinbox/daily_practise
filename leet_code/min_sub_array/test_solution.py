import unittest
from solution import Solution


class TestJump(unittest.TestCase):
    solution = Solution()

    def test_case_0(self):
        result = self.solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
        self.assertEqual(2, result)

    def test_case_1(self):
        result = self.solution.minSubArrayLen(4, [1, 4, 4])
        self.assertEqual(1, result)

    def test_case_2(self):
        result = self.solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1])
        self.assertEqual(0, result)


if __name__ == "__main__":
    unittest.main()
