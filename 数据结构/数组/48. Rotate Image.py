from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for i in range(len(matrix)):
            for j in range(i, len(matrix), 1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        n = len(matrix) - 1
        for i in range(len(matrix)):
            for j in range(len(matrix) // 2):
                matrix[i][j], matrix[i][n - j] = matrix[i][n - j], matrix[i][j]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
solution = Solution()
solution.rotate(matrix)
print(matrix)
