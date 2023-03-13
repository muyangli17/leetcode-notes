from typing import List


class Solution:
    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        for oneRow in matrix:
            if oneRow[0] > target:
                return False
            if oneRow[0] <= target <= oneRow[-1]:
                i = 0
                j = len(oneRow) - 1
                while i <= j:
                    mid = (i + j) // 2
                    if oneRow[mid] == target:
                        return True
                    if oneRow[mid] > target:
                        j = mid - 1
                    else:
                        i = mid + 1

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = 0
        c = len(matrix[0]) - 1
        while 0 <= r <= len(matrix) - 1 and 0 <= c <= len(matrix[0]) - 1:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1
            else:
                r += 1
        return False


matrix = [[1,1]]
target = 1
solution = Solution()
print(solution.searchMatrix(matrix, target))
