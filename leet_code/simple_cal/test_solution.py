import unittest
from solution import Solution


class TestJump(unittest.TestCase):
    solution = Solution()

    def test_case_0(self):
        s = "1 + 1"
        result = self.solution.calculate(s)
        expected = 2
        self.assertEqual(expected, result)

    def test_case_1(self):
        s = " 2-1 + 2 "
        result = self.solution.calculate(s)
        expected = 3
        self.assertEqual(expected, result)

    def test_case_2(self):
        s = "(1+(4+5+2)-3)+(6+8)"
        result = self.solution.calculate(s)
        expected = 23
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
