from typing import List


class Solution:
    def numIslands1(self, grid: List[List[str]]) -> int:
        islandnum = 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        toVisit = []

        def addNeighbour(sr: int, sc: int):
            if sr + 1 < m:
                if grid[sr + 1][sc] == "1" and not visited[sr + 1][sc]:
                    toVisit.append((sr + 1, sc))
                    visited[sr + 1][sc] = True
            if sr - 1 >= 0:
                if grid[sr - 1][sc] == "1" and not visited[sr - 1][sc]:
                    toVisit.append((sr - 1, sc))
                    visited[sr - 1][sc] = True
            if sc + 1 < n:
                if grid[sr][sc + 1] == "1" and not visited[sr][sc + 1]:
                    toVisit.append((sr, sc + 1))
                    visited[sr][sc + 1] = True
            if sc - 1 >= 0:
                if grid[sr][sc - 1] == "1" and not visited[sr][sc - 1]:
                    toVisit.append((sr, sc - 1))
                    visited[sr][sc - 1] = True

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    toVisit.append((i, j))
                    visited[i][j] = True
                    islandnum += 1
                    while len(toVisit) > 0:
                        (sr, sc) = toVisit.pop(0)
                        addNeighbour(sr, sc)

        return islandnum

    def numIslands2(self, grid: List[List[str]]) -> int:
        islandnum = 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def visit(sr: int, sc: int):
            visited[sr][sc] = True
            if sr + 1 < m:
                if grid[sr + 1][sc] == "1" and not visited[sr + 1][sc]:
                    visit(sr + 1, sc)
            if sr - 1 >= 0:
                if grid[sr - 1][sc] == "1" and not visited[sr - 1][sc]:
                    visit(sr - 1, sc)
            if sc + 1 < n:
                if grid[sr][sc + 1] == "1" and not visited[sr][sc + 1]:
                    visit(sr, sc + 1)
            if sc - 1 >= 0:
                if grid[sr][sc - 1] == "1" and not visited[sr][sc - 1]:
                    visit(sr, sc - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    islandnum += 1
                    visit(i, j)

        return islandnum


grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]

solution = Solution()
print(solution.numIslands2(grid=grid))
