import unittest
from solution import Solution


class TestJump(unittest.TestCase):
    solution = Solution()

    def test_case_0(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.solution.rotate(matrix)
        expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        self.assertEqual(expected, matrix)

    def test_case_1(self):
        matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        self.solution.rotate(matrix)
        expected = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
        self.assertEqual(expected, matrix)


if __name__ == "__main__":
    unittest.main()
