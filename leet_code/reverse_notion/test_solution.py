import unittest
from solution import Solution


class TestJump(unittest.TestCase):
    solution = Solution()

    def test_case_0(self):
        tokens = ["2", "1", "+", "3", "*"]
        result = self.solution.evalRPN(tokens)
        expected = 9
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
