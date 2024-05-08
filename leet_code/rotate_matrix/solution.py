from typing import List

# https://leetcode.com/problems/rotate-image/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        columns = len(matrix[0])
        temp_matrix = [[0 for i in range(rows)] for j in range(columns)]

        for row in range(rows):
            for column in range(columns):
                temp_matrix[column][rows - row - 1] = matrix[row][column]

        for row in range(rows):
            for column in range(columns):
                matrix[row][column] = temp_matrix[row][column]
