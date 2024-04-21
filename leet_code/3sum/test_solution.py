import unittest
from solution import Solution


class TestJump(unittest.TestCase):
    solution = Solution()

    def test_case_0(self):
        result = self.solution.threeSum([-1, 0, 1, 2, -1, -4])
        self.assertEqual([[-1, -1, 2], [-1, 0, 1]], result)

    def test_case_1(self):
        result = self.solution.threeSum([0, 1, 1])
        self.assertEqual([], result)

    def test_case_2(self):
        result = self.solution.threeSum([0, 0, 0])
        self.assertEqual([0, 0, 0], result)


if __name__ == "__main__":
    unittest.main()
