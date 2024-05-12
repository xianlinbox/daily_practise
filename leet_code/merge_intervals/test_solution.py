import unittest
from solution import Solution


class TestJump(unittest.TestCase):
    solution = Solution()

    def test_case_0(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        result = self.solution.merge(intervals)
        expected = [[1, 6], [8, 10], [15, 18]]
        self.assertEqual(expected, result)

    # def test_case_1(self):
    #     intervals = [[1, 4], [4, 5]]
    #     result = self.solution.merge(intervals)
    #     expected = [[1, 5]]
    #     self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
