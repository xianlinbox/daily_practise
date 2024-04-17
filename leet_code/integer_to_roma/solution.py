from typing import List


class Solution:
    def intToRoman(self, num: int) -> str:
        rules = [
            ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
            ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
        ]

        #         I             1
        # V             5
        # X             10
        # L             50
        # C             100
        # D             500
        # M             1000

        digits = list(str(num))
        digits.reverse()
        result = ""
        for i in range(0, len(digits)):
            result = rules[i][int(digits[i]) - 1] + result
        return result
