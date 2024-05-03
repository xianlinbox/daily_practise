from typing import List


# https://leetcode.com/problems/game-of-life/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows = len(board)
        columns = len(board[0])
        surround_lives_board = [[0 for _ in range(columns)] for _ in range(rows)]
        for row in range(rows):
            for column in range(columns):
                surround_lives_board[row][column] = self.calculate_surround_lives(
                    board, row, column
                )

        for row in range(rows):
            for column in range(columns):
                surround_lives = surround_lives_board[row][column]
                if surround_lives < 2 or surround_lives > 3:
                    board[row][column] = 0
                elif surround_lives == 3:
                    board[row][column] = 1

    def calculate_surround_lives(
        self, board: List[List[int]], row: int, column: int
    ) -> int:
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
            if 0 <= i < rows and 0 <= j < columns:
                result += board[i][j]
        return result
