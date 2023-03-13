from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        number = 1
        for k in range(n):
            for j in range(k, n - 1 - k, 1):
                matrix[k][j] = number
                number += 1
            for i in range(k, n - 1 - k, 1):
                matrix[i][n - 1 - k] = number
                number += 1
            for j in range(n - 1 - k, k, -1):
                matrix[n - 1 - k][j] = number
                number += 1
            for i in range(n - 1 - k, k, -1):
                matrix[i][k] = number
                number += 1

        if n % 2 == 1:
            matrix[n // 2][n // 2] = number

        return matrix


n = 3
solution = Solution()
print(solution.generateMatrix(n))
