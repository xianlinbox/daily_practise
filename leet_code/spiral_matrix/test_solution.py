import unittest
from solution import Solution


class TestJump(unittest.TestCase):
    solution = Solution()

    def test_case_0(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = self.solution.spiralOrder(matrix)
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(expected, result)

    # def test_case_1(self):
    #     matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    #     result = self.solution.spiralOrder(matrix)
    #     expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    #     self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
