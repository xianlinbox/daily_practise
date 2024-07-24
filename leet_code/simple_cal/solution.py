from typing import List

# https://leetcode.com/problems/basic-calculator/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def calculate(self, s: str) -> int:
        chars = list(s.replace(" ",""))
        operators = []
        numbers = []
        temp = None
        isNegative = False
        for i in range(0,len(chars)):
            char = chars[i]
            match char:
                case '+' | '-':
                    if temp != None:
                        if isNegative:
                            temp = int("-"+str(temp))
                            operators.pop()
                            isNegative=False
                        numbers.append(temp)
                        temp = None
                    if len(numbers) >= 2:
                        while operators:
                            if operators[-1] == "(":
                                break
                            op = operators.pop()
                            numbers.append(self.calcaulte(numbers, op))
                    operators.append(char)
                case '(':
                    operators.append(char)
                case ')':
                    if temp != None:
                        if isNegative:
                            temp = int("-"+str(temp))
                            operators.pop()
                            isNegative= False
                        numbers.append(temp)
                        temp = None
                    curr_op = operators.pop()
                    while  curr_op != '(':
                        numbers.append(self.calcaulte(numbers, curr_op))
                        curr_op = operators.pop()
                case _:
                    if temp == None:
                        isNegative = i >= 1 and chars[i-1] == "-" and (i-2<0 or chars[i-2]=='(')
                        temp = int(char)
                    else:
                        temp = temp * 10 + int(char)
                    
        if temp != None: 
            if isNegative:
                temp = int("-"+str(temp))
                operators.pop()
                isNegative= False
            numbers.append(temp)
        if len(numbers) >=2:
            return self.calcaulte(numbers, operators.pop())
        else:
            result = numbers.pop()
            if operators:
                result = int("-"+str(result))
            return result

    def calcaulte(self, numbers, op) -> str:
        number_1 = numbers.pop()
        number_2 = numbers.pop()
        if op == '+':
           return number_2+ number_1
        else:
            return number_2 - number_1 
    

