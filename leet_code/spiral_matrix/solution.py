from typing import List

# https://leetcode.com/problems/spiral-matrix/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up = 0
        down = len(matrix)
        left = 0
        right = len(matrix[0])
        result = []

        while left <= right and up <= down:
            for i in range(left, right):
                result.append(matrix[up][i])
            up += 1

            for i in range(up, down):
                result.append(matrix[i][right])
            right -= 1

            for i in range(right, left, -1):
                result.append(matrix[down][i])
            down -= 1

            for i in range(down, up, -1):
                result.append(matrix[i][left])
            left += 1

        return result
