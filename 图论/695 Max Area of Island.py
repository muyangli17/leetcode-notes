from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        areas = [0]

        def visit(sr: int, sc: int, nowarea: int) -> int:
            visited[sr][sc] = True
            nowarea += 1
            if sr + 1 < m:
                if grid[sr + 1][sc] == 1 and not visited[sr + 1][sc]:
                    nowarea = visit(sr + 1, sc, nowarea)
            if sr - 1 >= 0:
                if grid[sr - 1][sc] == 1 and not visited[sr - 1][sc]:
                    nowarea = visit(sr - 1, sc, nowarea)
            if sc + 1 < n:
                if grid[sr][sc + 1] == 1 and not visited[sr][sc + 1]:
                    nowarea = visit(sr, sc + 1, nowarea)
            if sc - 1 >= 0:
                if grid[sr][sc - 1] == 1 and not visited[sr][sc - 1]:
                    nowarea = visit(sr, sc - 1, nowarea)
            return nowarea

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    area = 0
                    area = visit(i, j, area)
                    areas.append(area)

        return max(areas)


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

solution = Solution()
print(solution.maxAreaOfIsland(grid=grid))
