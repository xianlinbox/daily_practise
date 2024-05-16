from typing import List

# https://leetcode.com/problems/min-stack/description/?envType=study-plan-v2&envId=top-interview-150


class MinStack:

    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        self.data.append(val)

    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return min(self.data)
