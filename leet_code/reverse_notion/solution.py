from typing import List

# https://leetcode.com/problems/min-stack/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []

        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                numbers.append(int(token))
            else:
                a, b = numbers.pop(), numbers.pop()
                match token:
                    case "+":
                        numbers.append(a + b)
                    case "-":
                        numbers.append(b - a)
                    case "/":
                        numbers.append(int(b / a))
                    case "*":
                        numbers.append(a * b)
        return numbers[0]
