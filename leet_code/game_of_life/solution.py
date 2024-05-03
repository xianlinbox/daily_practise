from typing import List


# https://leetcode.com/problems/game-of-life/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        for row in range(len(board)):
            for column in range(len(board[0])):
                item = board[row][column]
                surround_lives = self.calculate_surround_lives(board, row, column)

                if surround_lives < 2 or surround_lives > 3:
                    board[row][column] = 0
                elif surround_lives == 3:
                    board[row][column] = 1

    def calculate_surround_lives(board: List[List[int]], row: int, column: int) -> int:
        rows = len(board)
        columns = len(board[0])
        surround_indexes = [
            (row - 1, column - 1),
            (row - 1, column),
            (row - 1, column + 1),
            (row, column - 1),
            (row, column + 1),
            (row + 1, column - 1),
            (row + 1, column),
            (row + 1, column + 1),
        ]
        result = 0
        for i, j in surround_indexes:
            if 0 <= i < rows and 0 <= j < column:
                result += board[i][j]
        return result
