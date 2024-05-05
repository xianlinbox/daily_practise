from typing import List

# https://leetcode.com/problems/set-matrix-zeroes/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        columns = len(matrix[0])
        zero_rows = set()
        zero_columns = set()
        for row in range(rows):
            for column in range(columns):
                if matrix[row][column] == 0:
                    zero_rows.add(row)
                    zero_columns.add(column)

        for row in range(rows):
            for column in range(columns):
                if row in zero_rows or column in zero_columns:
                    matrix[row][column] = 0
