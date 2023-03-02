from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        result = [[0] * n for _ in range(m)]

        directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]

        def searchZero(sr: int, sc: int) -> int:
            depth = 0
            inToVisited = [[False] * n for _ in range(m)]
            toVisit = [[sr, sc]]
            inToVisited[sr][sc] = True

            while len(toVisit) > 0:
                nextToVisit = []

                for point in toVisit:
                    [x, y] = point
                    if mat[x][y] == 0:
                        return depth

                    for direction in directions:
                        nextX = x + direction[0]
                        nextY = y + direction[1]
                        if 0 <= nextX < m and 0 <= nextY < n and not inToVisited[nextX][nextY]:
                            nextToVisit.append([nextX, nextY])
                            inToVisited[nextX][nextY] = True

                toVisit = nextToVisit
                depth += 1

        for i in range(m):
            for j in range(n):
                result[i][j] = searchZero(i, j)
        return result


mat = [[0, 0, 0], [0, 1, 1], [1, 0, 0]]
solution = Solution()
print(solution.updateMatrix(mat=mat))
