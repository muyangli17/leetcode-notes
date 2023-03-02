from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        subIslandNum = 0
        m = len(grid1)
        n = len(grid1[0])
        visited = [[False] * n for _ in range(m)]

        def visit(sr: int, sc: int) -> bool:
            contain = (grid1[sr][sc] == 1)
            visited[sr][sc] = True
            if sr + 1 < m:
                if grid2[sr + 1][sc] == 1 and not visited[sr + 1][sc]:
                    contain = visit(sr + 1, sc) and contain
            if sr - 1 >= 0:
                if grid2[sr - 1][sc] == 1 and not visited[sr - 1][sc]:
                    contain = visit(sr - 1, sc) and contain
            if sc + 1 < n:
                if grid2[sr][sc + 1] == 1 and not visited[sr][sc + 1]:
                    contain = visit(sr, sc + 1) and contain
            if sc - 1 >= 0:
                if grid2[sr][sc - 1] == 1 and not visited[sr][sc - 1]:
                    contain = visit(sr, sc - 1) and contain
            return contain

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and not visited[i][j]:
                    if visit(i, j):
                        subIslandNum += 1

        return subIslandNum


grid1 = [[1, 1, 1, 0, 0],
         [0, 1, 1, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0],
         [1, 1, 0, 1, 1]]
grid2 = [[1, 1, 1, 0, 0],
         [0, 0, 1, 1, 1],
         [0, 1, 0, 0, 0],
         [1, 0, 1, 1, 0],
         [0, 1, 0, 1, 0]]

solution = Solution()
print(solution.countSubIslands(grid1=grid1, grid2=grid2))
