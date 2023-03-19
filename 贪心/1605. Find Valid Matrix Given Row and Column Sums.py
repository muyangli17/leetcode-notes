from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        s = sum(rowSum)

        rowNum = len(rowSum)
        colNum = len(colSum)

        matrix = [[0] * colNum for _ in range(rowNum)]

        r = 0
        c = 0
        while s > 0:
            if rowSum[r] == 0:
                r += 1
            elif colSum[c] == 0:
                c += 1
            elif rowSum[r] <= colSum[c]:
                matrix[r][c] = rowSum[r]
                s -= rowSum[r]
                colSum[c] -= rowSum[r]
                rowSum[r] = 0
            else:
                matrix[r][c] = colSum[c]
                s -= colSum[c]
                rowSum[r] -= colSum[c]
                colSum[c] = 0
        return matrix


rowSum = [3,8]
colSum = [4,7]
solution = Solution()
print(solution.restoreMatrix(rowSum=rowSum, colSum=colSum))
