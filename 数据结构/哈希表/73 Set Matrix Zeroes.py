from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroRow = dict()
        zeroCol = dict()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroRow[i] = True
                    zeroCol[j] = True

        for key in zeroRow:
            for j in range(len(matrix[0])):
                matrix[key][j] = 0
        for key in zeroCol:
            for i in range(len(matrix)):
                matrix[i][key] = 0


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
solution = Solution()
solution.setZeroes(matrix)
print(matrix)
