import unittest
from solution import Solution


class TestJump(unittest.TestCase):
    solution = Solution()

    def test_case_0(self):
        intervals = [[1, 3], [6, 9]]
        newInterval = [2, 5]

        result = self.solution.insert(intervals, newInterval)
        expected = [[1, 5], [6, 9]]

        self.assertEqual(expected, result)

    def test_case_1(self):
        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        newInterval = [4, 8]

        result = self.solution.insert(intervals, newInterval)
        expected = [[1, 2], [3, 10], [12, 16]]

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
