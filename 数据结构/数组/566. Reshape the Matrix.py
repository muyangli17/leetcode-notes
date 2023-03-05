from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if not m * n == r * c:
            return mat

        res = [[0] * c for _ in range(r)]

        for i in range(m * n):
            res[i // c][i % c] = mat[i // n][i % n]

        return res


mat = [[1, 2], [3, 4]]
r = 1
c = 4
solution = Solution()
print(solution.matrixReshape(mat=mat, r=r, c=c))
