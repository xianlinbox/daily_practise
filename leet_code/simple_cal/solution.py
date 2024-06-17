from typing import List

# https://leetcode.com/problems/basic-calculator/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def calculate(self, s: str) -> int:
        operators = []
        numbers = []
        for char in s:
            match char:
                case ' ':
                    continue
                case '+' | '-':
                    if len(numbers) >= 2:
                        op = operators.pop()
                        numbers.append(self.calcaulte(numbers, op))
                    operators.append(char)
                case '(':
                    operators.append(char)
                case ')':
                    curr_op = operators.pop()
                    while  curr_op != '(':
                        self.calcaulte(numbers, curr_op)
                        curr_op = operators.pop()
                case _:
                    numbers.append(int(char))
        
        return self.calcaulte(numbers, operators.pop())
    
    def calcaulte(self, numbers, op) -> str:
        number_1 = numbers.pop()
        number_2 = numbers.pop()
        if op == '+':
           return number_2+ number_1
        else:
            return number_2 - number_1 
    

