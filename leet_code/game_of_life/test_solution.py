import unittest
from solution import Solution


class TestJump(unittest.TestCase):
    solution = Solution()

    def test_case_0(self):
        board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
        self.solution.gameOfLife(board)
        expected = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
        self.assertEqual(expected, board)

    def test_case_1(self):
        board = [[1, 1], [1, 0]]
        self.solution.gameOfLife(board)
        expected = [[1, 1], [1, 1]]
        self.assertEqual(expected, board)


if __name__ == "__main__":
    unittest.main()
