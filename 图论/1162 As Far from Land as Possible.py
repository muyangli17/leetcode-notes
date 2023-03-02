from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        toVisit = []
        distance = [[1000] * n for _ in range(m)]
        maxDistance = -1

        def visit(sr: int, sc: int):
            if sr + 1 < m:
                if not visited[sr + 1][sc]:
                    toVisit.append((sr + 1, sc))
                    visited[sr + 1][sc] = True
                    distance[sr + 1][sc] = min(distance[sr][sc] + 1, distance[sr + 1][sc])
            if sr - 1 >= 0:
                if not visited[sr - 1][sc]:
                    toVisit.append((sr - 1, sc))
                    visited[sr - 1][sc] = True
                    distance[sr - 1][sc] = min(distance[sr][sc] + 1, distance[sr - 1][sc])
            if sc + 1 < n:
                if not visited[sr][sc + 1]:
                    toVisit.append((sr, sc + 1))
                    visited[sr][sc + 1] = True
                    distance[sr][sc + 1] = min(distance[sr][sc] + 1, distance[sr][sc + 1])
            if sc - 1 >= 0:
                if not visited[sr][sc - 1]:
                    toVisit.append((sr, sc - 1))
                    visited[sr][sc - 1] = True
                    distance[sr][sc - 1] = min(distance[sr][sc] + 1, distance[sr][sc - 1])

        uniform = True

        for i in range(m):
            for j in range(n):
                if grid[i][j] != grid[0][0]:
                    uniform = False
        if uniform:
            return -1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    distance[i][j] = 0
                    toVisit.append((i, j))
                    visited[i][j] = True
                    maxDistance = 0

        while len(toVisit) > 0:
            (sr, sc) = toVisit.pop(0)
            visit(sr, sc)

        for i in range(m):
            maxDistance = max(maxDistance, max(distance[i]))

        return maxDistance


grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
solution = Solution()
print(solution.maxDistance(grid=grid))
