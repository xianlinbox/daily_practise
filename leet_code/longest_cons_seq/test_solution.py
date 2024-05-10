import unittest
from solution import Solution


class TestJump(unittest.TestCase):
    solution = Solution()

    def test_case_0(self):
        nums = [100, 4, 200, 1, 3, 2]
        result = self.solution.longestConsecutive(nums)
        self.assertEqual(4, result)

    def test_case_1(self):
        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        result = self.solution.longestConsecutive(nums)
        self.assertEqual(9, result)


if __name__ == "__main__":
    unittest.main()
