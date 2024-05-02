from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check = {}
        column_check = {}
        matrix_check = {}
        for i in range(9):
            row_check[i] = []
            column_check[i] = []
            matrix_check[i] = []

        for row in range(len(board)):
            for column in range(len(board[0])):
                item = board[row][column]
                if item == ".":
                    continue
                matrix_index = int(row / 3) * 3 + int(column / 3)
                if (
                    item not in row_check[row]
                    and item not in column_check[column]
                    and item not in matrix_check[matrix_index]
                ):
                    row_check[row].append(item)
                    column_check[column].append(item)
                    matrix_check[matrix_index].append(item)
                else:
                    return False
        return True
