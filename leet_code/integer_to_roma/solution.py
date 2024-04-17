from typing import List


class Solution:
    def intToRoman(self, num: int) -> str:
        rules = [
            ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
            ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
            ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
            ["M", "MM", "MMM"],
        ]
        digits = list(str(num))
        digits.reverse()
        result = ""
        for i in range(0, len(digits)):
            result = rules[i][int(digits[i]) - 1] + result
        return result
