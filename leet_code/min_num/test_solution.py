import unittest
from solution import Solution


class TestJump(unittest.TestCase):
    solution = Solution()

    def test_case_0(self):
        points = [[10, 16], [2, 8], [1, 6], [7, 12]]
        result = self.solution.findMinArrowShots(points)
        expected = 2
        self.assertEqual(expected, result)

    def test_case_1(self):
        points = [[1, 2], [3, 4], [5, 6], [7, 8]]
        result = self.solution.findMinArrowShots(points)
        expected = 4

    #     self.assertEqual(expected, result)

    def test_case_2(self):
        points = [[1, 2], [2, 3], [3, 4], [4, 5]]
        result = self.solution.findMinArrowShots(points)
        expected = 2
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
