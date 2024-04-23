import unittest
from solution import Solution


class TestJump(unittest.TestCase):
    solution = Solution()

    def test_case_0(self):
        result = self.solution.twoSum([2, 7, 11, 15], 9)
        self.assertEqual([[2, 7]], result)

    def test_case_1(self):
        result = self.solution.twoSum([2, 3, 4], 6)
        self.assertEqual([[1, 3]], result)

    def test_case_2(self):
        result = self.solution.twoSum([-1, 0], -1)
        self.assertEqual([[1, 2]], result)


if __name__ == "__main__":
    unittest.main()
