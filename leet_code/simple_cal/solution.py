from typing import List

# https://leetcode.com/problems/basic-calculator/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def calculate(self, s: str) -> int:
        operators = []
        numbers = []
        #  "(1+(4+5+2)-3)+(6+8)"
        for char in s:
            match char:
                case ' ':
                    continue
                case '+' | '-':
                    if len(numbers) >= 2:
                        while not operators and operators[-1] != '(':
                            op = operators.pop()
                            numbers.append(self.calcaulte(numbers, op))
                    operators.append(char)
                case '(':
                    operators.append(char)
                case ')':
                    curr_op = operators.pop()
                    while  curr_op != '(':
                        numbers.append(self.calcaulte(numbers, curr_op))
                        curr_op = operators.pop()
                case _:
                    numbers.append(int(char))
            print(numbers)
            print("****")
            print(operators)
            print("###")
        if len(numbers) >=2:
            return self.calcaulte(numbers, operators.pop())
        else:
            return numbers.pop()
    
    def calcaulte(self, numbers, op) -> str:
        number_1 = numbers.pop()
        number_2 = numbers.pop()
        if op == '+':
           return number_2+ number_1
        else:
            return number_2 - number_1 
    

