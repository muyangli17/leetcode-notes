from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # 所有入度为0的点的集合即为所求 (Zorn's lemma?)
        # The collection of points whose in-degree is 0 (Zorn's lemma?)
        inDegree = [0] * n
        for edge in edges:
            inDegree[edge[1]] += 1

        res = []
        for i in range(n):
            if inDegree[i] == 0:
                res.append(i)
        return res
