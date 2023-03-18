from typing import List


class Solution:
    def shortestPathBinaryMatrix1(self, grid: List[List[int]]) -> int:
        # 此解法超时
        n = len(grid)
        shortest = [[1000] * n for _ in range(n)]
        toVisit = [[0, 0]]
        directions = [[x, y] for x in range(-1, 2, 1) for y in range(-1, 2, 1)]
        directions.remove([0, 0])

        def visit(visitLoc):
            [sr, sc] = visitLoc
            for direction in directions:
                nextLoc = [sr + direction[0], sc + direction[1]]
                if 0 <= nextLoc[0] < n and 0 <= nextLoc[1] < n:
                    if grid[nextLoc[0]][nextLoc[1]] == 0:
                        if shortest[nextLoc[0]][nextLoc[1]] > shortest[sr][sc] + 1:
                            shortest[nextLoc[0]][nextLoc[1]] = shortest[sr][sc] + 1
                            toVisit.append(nextLoc)

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        shortest[0][0] = 1
        while len(toVisit) > 0:
            visit(toVisit.pop())

        if shortest[n - 1][n - 1] == 1000:
            return -1

        return shortest[n - 1][n - 1]

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1 or n == 0:
            return -1

        directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

        depth = 1
        toVisit = [[0, 0]]

        while len(toVisit) > 0:
            nextToVisit = []

            for point in toVisit:
                if point == [n - 1, n - 1]:
                    return depth

                [sr, sc] = point
                grid[sr][sc] = 1

                for direction in directions:
                    x = sr + direction[0]
                    y = sc + direction[1]
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                        grid[x][y] = 1  # 提前封堵该格
                        nextToVisit.append([x, y])

            toVisit = nextToVisit
            depth += 1
        return -1

    def shortestPathBinaryMatrix3(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0:
            return -1
        cur = [(0, 0)]
        grid[0][0] = -1
        step = -2
        while len(cur) != 0:
            ncur = []
            for c in cur:
                x = c[0]
                y = c[1]
                if x - 1 >= 0:
                    if y - 1 >= 0:
                        if grid[x - 1][y - 1] == 0:
                            grid[x - 1][y - 1] = step
                            ncur.append((x - 1, y - 1))
                        if grid[x - 1][y] == 0:
                            grid[x - 1][y] = step
                            ncur.append((x - 1, y))
                    if y + 1 < n:
                        if grid[x - 1][y + 1] == 0:
                            grid[x - 1][y + 1] = step
                            ncur.append((x - 1, y + 1))

                if y - 1 >= 0:
                    if grid[x][y - 1] == 0:
                        grid[x][y - 1] = step
                        ncur.append((x, y - 1))
                if y + 1 < n:
                    if grid[x][y + 1] == 0:
                        grid[x][y + 1] = step
                        ncur.append((x, y + 1))

                if x + 1 < n:
                    if y - 1 >= 0:
                        if grid[x + 1][y - 1] == 0:
                            grid[x + 1][y - 1] = step
                            ncur.append((x + 1, y - 1))
                        if grid[x + 1][y] == 0:
                            grid[x + 1][y] = step
                            ncur.append((x + 1, y))
                    if y + 1 < n:
                        if grid[x + 1][y + 1] == 0:
                            grid[x + 1][y + 1] = step
                            ncur.append((x + 1, y + 1))
            # print(ncur)
            cur = ncur
            step -= 1
        # print(grid)
        if grid[-1][-1] < 0:
            return -grid[-1][-1]

        return -1


grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]

solution = Solution()
print(solution.shortestPathBinaryMatrix(grid=grid))
