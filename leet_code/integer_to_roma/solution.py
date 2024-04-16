from typing import List


class Solution:
    def intToRoman(self, num: int) -> str:
        digits = list(str(num))
        digits.reverse()
        result = ""
        for i in range(0, len(digits)):
            digit = int(digits[i])
            match i:
                case 0:
                    if digit < 5:
                        result += "I" * digit
                    elif digit == 5:
                        result += "V"
                    else:
                        result += "V" + (digit - 5) * "I"
        return result
