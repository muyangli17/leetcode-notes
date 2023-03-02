from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        visited = [[False]*n for _ in range(m)]
        toColor = [(sr, sc)]
        visited[sr][sc] = True

        def addNeighbour(sr: int, sc: int, localColor: int):
            if sr + 1 < m:
                if image[sr + 1][sc] == localColor and not visited[sr + 1][sc]:
                    toColor.append((sr + 1, sc))
                    visited[sr + 1][sc] = True
            if sr - 1 >= 0:
                if image[sr - 1][sc] == localColor and not visited[sr - 1][sc]:
                    toColor.append((sr - 1, sc))
                    visited[sr - 1][sc] = True
            if sc + 1 < n:
                if image[sr][sc + 1] == localColor and not visited[sr][sc + 1]:
                    toColor.append((sr, sc + 1))
                    visited[sr][sc + 1] = True
            if sc - 1 >= 0:
                if image[sr][sc - 1] == localColor and not visited[sr][sc - 1]:
                    toColor.append((sr, sc - 1))
                    visited[sr][sc - 1] = True

        while len(toColor) > 0:
            (sr, sc) = toColor.pop(0)
            addNeighbour(sr, sc, image[sr][sc])
            image[sr][sc] = color

        return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2


solution = Solution()
print(solution.floodFill(image=image, sr=sr, sc=sc, color=color))
