from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m = len(heights)
        n = len(heights[0])
        toVisit = []
        PacificAvailable = [[0] * n for _ in range(m)]
        AtlanticAvailable = [[0] * n for _ in range(m)]

        def addtoVisit(sr, sc, Pacific):
            if not (sr, sc) in toVisit:
                toVisit.append((sr, sc))
                if Pacific:
                    PacificAvailable[sr][sc] = 1
                else:
                    AtlanticAvailable[sr][sc] = 1

        def visit(sr: int, sc: int, Pacific: bool):
            visited[sr][sc] = True
            if sr + 1 < m:
                if not visited[sr + 1][sc]:
                    if heights[sr + 1][sc] >= heights[sr][sc]:
                        addtoVisit(sr + 1, sc, Pacific)
            if sr - 1 >= 0:
                if not visited[sr - 1][sc]:
                    if heights[sr - 1][sc] >= heights[sr][sc]:
                        addtoVisit(sr - 1, sc, Pacific)
            if sc + 1 < n:
                if not visited[sr][sc + 1]:
                    if heights[sr][sc + 1] >= heights[sr][sc]:
                        addtoVisit(sr, sc + 1, Pacific)
            if sc - 1 >= 0:
                if not visited[sr][sc - 1]:
                    if heights[sr][sc - 1] >= heights[sr][sc]:
                        addtoVisit(sr, sc - 1, Pacific)

        # Pacific
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            addtoVisit(i, 0, Pacific=True)
        for j in range(n):
            addtoVisit(0, j, Pacific=True)
            PacificAvailable[0][j] = 1
        while len(toVisit) > 0:
            (sr, sc) = toVisit.pop(0)
            visit(sr, sc, Pacific=True)

        # Atlantic
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            addtoVisit(i, n - 1, Pacific=False)
        for j in range(n):
            addtoVisit(m - 1, j, Pacific=False)
        while len(toVisit) > 0:
            (sr, sc) = toVisit.pop(0)
            visit(sr, sc, Pacific=False)

        bothAvailable = []
        for i in range(m):
            for j in range(n):
                if PacificAvailable[i][j] == 1 and AtlanticAvailable[i][j] == 1:
                    bothAvailable.append([i, j])

        return bothAvailable


heights = [[1, 2, 2, 3, 5],
           [3, 2, 3, 4, 4],
           [2, 4, 5, 3, 1],
           [6, 7, 1, 4, 5],
           [5, 1, 1, 2, 4]]
solution = Solution()
print(solution.pacificAtlantic(heights=heights))
