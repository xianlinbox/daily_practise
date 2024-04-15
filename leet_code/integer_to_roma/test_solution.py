import unittest
from solution import Solution


class TestJump(unittest.TestCase):
    solution = Solution()

    def test_case_0(self):
        self.assertEqual("III", self.solution.intToRoman(3))

    def test_case_1(self):
        self.assertEqual("LVIII", self.solution.intToRoman(58))

    def test_case_2(self):
        self.assertEqual("MCMXCIV", self.solution.intToRoman(1994))


if __name__ == "__main__":
    unittest.main()
