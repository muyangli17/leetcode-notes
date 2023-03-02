from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        enclavesArea = 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def fill(sr: int, sc: int):
            visited[sr][sc] = True
            if sr + 1 < m:
                if grid[sr + 1][sc] == 1 and not visited[sr + 1][sc]:
                    fill(sr + 1, sc)
            if sr - 1 >= 0:
                if grid[sr - 1][sc] == 1 and not visited[sr - 1][sc]:
                    fill(sr - 1, sc)
            if sc + 1 < n:
                if grid[sr][sc + 1] == 1 and not visited[sr][sc + 1]:
                    fill(sr, sc + 1)
            if sc - 1 >= 0:
                if grid[sr][sc - 1] == 1 and not visited[sr][sc - 1]:
                    fill(sr, sc - 1)

        def visit(sr: int, sc: int, area: int) -> int:
            visited[sr][sc] = True
            area += 1
            if sr + 1 < m:
                if grid[sr + 1][sc] == 1 and not visited[sr + 1][sc]:
                    area = visit(sr + 1, sc, area)
            if sr - 1 >= 0:
                if grid[sr - 1][sc] == 1 and not visited[sr - 1][sc]:
                    area = visit(sr - 1, sc, area)
            if sc + 1 < n:
                if grid[sr][sc + 1] == 1 and not visited[sr][sc + 1]:
                    area = visit(sr, sc + 1, area)
            if sc - 1 >= 0:
                if grid[sr][sc - 1] == 1 and not visited[sr][sc - 1]:
                    area = visit(sr, sc - 1, area)
            return area

        for i in range(m):
            if grid[i][0] == 1 and not visited[i][0]:
                fill(i, 0)
            if grid[i][n - 1] == 1 and not visited[i][n - 1]:
                fill(i, n - 1)

        for j in range(n):
            if grid[0][j] == 1 and not visited[0][j]:
                fill(0, j)
            if grid[m - 1][j] == 1 and not visited[m - 1][j]:
                fill(m - 1, j)

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 1 and not visited[i][j]:
                    enclavesArea = visit(i, j, enclavesArea)

        return enclavesArea


grid = [[0, 0, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]]

solution = Solution()
print(solution.numEnclaves(grid=grid))
