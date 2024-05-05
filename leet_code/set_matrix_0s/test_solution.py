import unittest
from solution import Solution


class TestJump(unittest.TestCase):
    solution = Solution()

    def test_case_0(self):
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        self.solution.setZeroes(matrix)
        expected = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        self.assertEqual(expected, matrix)

    def test_case_1(self):
        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        self.solution.setZeroes(matrix)
        expected = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
        self.assertEqual(expected, matrix)


if __name__ == "__main__":
    unittest.main()
