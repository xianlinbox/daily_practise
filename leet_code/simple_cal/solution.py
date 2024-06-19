from typing import List

# https://leetcode.com/problems/basic-calculator/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def calculate(self, s: str) -> int:
        operators = []
        numbers = []
        #  "(1+(4+5+2)-3)+(6+8)"
        temp = -1
        for char in s:
            print(char)
            match char:
                case ' ':
                    continue
                case '+' | '-':
                    if temp != -1:
                        numbers.append(temp)
                        temp = -1
                    if len(numbers) >= 2:
                        while operators:
                            if operators[-1] == "(":
                                break
                            print("hanlde one")
                            op = operators.pop()
                            numbers.append(self.calcaulte(numbers, op))
                    operators.append(char)
                case '(':
                    operators.append(char)
                case ')':
                    if temp != -1:
                        numbers.append(temp)
                        temp = -1
                    curr_op = operators.pop()
                    while  curr_op != '(':
                        numbers.append(self.calcaulte(numbers, curr_op))
                        curr_op = operators.pop()
                case _:
                    if temp == -1:
                        temp = int(char)
                    else:
                        temp = temp * 10 + int(char)
            print(numbers)
            print(operators)
        if temp != -1: 
            numbers.append(temp)
    
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
    

