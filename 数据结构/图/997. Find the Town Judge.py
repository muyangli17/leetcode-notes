from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        oDegree = [0] * (n + 1)
        iDegree = [0] * (n + 1)

        for edge in trust:
            oDegree[edge[0]] += 1
            iDegree[edge[1]] += 1

        find = -1
        for i in range(1, n + 1, 1):
            if oDegree[i] == 0 and iDegree[i] == n - 1:
                if find == -1:
                    find = i
                else:
                    return -1

        return find


n = 4
trust = [[1, 3], [2, 3], [1, 4], [2, 4]]
solution = Solution()
print(solution.findJudge(n=n, trust=trust))
