from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            digits = [False] * 10
            for j in range(9):
                if board[i][j] != ".":
                    if digits[int(board[i][j])]:
                        return False
                    else:
                        digits[int(board[i][j])] = True

        for i in range(9):
            digits = [False] * 10
            for j in range(9):
                if board[j][i] != ".":
                    if digits[int(board[j][i])]:
                        return False
                    else:
                        digits[int(board[j][i])] = True

        for i in range(3):
            for j in range(3):
                digits = [False] * 10
                for r in range(3 * i, 3 * i + 3):
                    for c in range(3 * j, 3 * j + 3):
                        if board[r][c] != ".":
                            if digits[int(board[r][c])]:
                                return False
                            else:
                                digits[int(board[r][c])] = True
        return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

solution = Solution()
print(solution.isValidSudoku(board=board))
