from typing import List

# https://leetcode.com/problems/min-stack/description/?envType=study-plan-v2&envId=top-interview-150


class MinStack:

    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        if not self.data:
            self.data.append([val, val])
        else:
            if self.data[-1][1] < val:
                self.data.append([val, self.data[-1][1]])
            else:
                self.data.append([val, val])

    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.data[-1][1]
