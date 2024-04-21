import unittest
from solution import Solution


class TestJump(unittest.TestCase):
    solution = Solution()

    def test_case_0(self):
        result = self.solution.max([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
        self.assertEqual(3, result)


if __name__ == "__main__":
    unittest.main()
