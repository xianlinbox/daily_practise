import unittest
from solution import Solution


class TestJump(unittest.TestCase):
    solution = Solution()

    def test_case_0(self):
        self.assertEqual("III", self.solution.intToRoman(3))

    def test_case_0_1(self):
        self.assertEqual("V", self.solution.intToRoman(5))

    def test_case_0_2(self):
        self.assertEqual("IX", self.solution.intToRoman(9))

    def test_case_0_3(self):
        self.assertEqual("IV", self.solution.intToRoman(4))

    def test_case_1(self):
        self.assertEqual("LVIII", self.solution.intToRoman(58))

    def test_case_1_1(self):
        self.assertEqual("XXXVIII", self.solution.intToRoman(38))

    def test_case_1_2(self):
        self.assertEqual("LXVIII", self.solution.intToRoman(68))

    def test_case_2(self):
        self.assertEqual("CXCIV", self.solution.intToRoman(194))

    def test_case_2_1(self):
        self.assertEqual("CDXCIV", self.solution.intToRoman(494))

    def test_case_2_2(self):
        self.assertEqual("CMXCIV", self.solution.intToRoman(994))

    def test_case_3(self):
        self.assertEqual("MCMXCIV", self.solution.intToRoman(1994))

    def test_case_4(self):
        self.assertEqual("X", self.solution.intToRoman(10))

    def test_case_4_1(self):
        self.assertEqual("C", self.solution.intToRoman(100))

    def test_case_4_2(self):
        self.assertEqual("M", self.solution.intToRoman(1000))


if __name__ == "__main__":
    unittest.main()
