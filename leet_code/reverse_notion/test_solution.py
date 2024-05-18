import unittest
from solution import Solution


class TestJump(unittest.TestCase):
    solution = Solution()

    def test_case_0(self):
        tokens = ["2", "1", "+", "3", "*"]
        result = self.solution.evalRPN(tokens)
        expected = 9
        self.assertEqual(expected, result)

    def test_case_1(self):
        tokens = ["4", "13", "5", "/", "+"]
        result = self.solution.evalRPN(tokens)
        expected = 6
        self.assertEqual(expected, result)

    def test_case_2(self):
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        result = self.solution.evalRPN(tokens)
        expected = 22
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
