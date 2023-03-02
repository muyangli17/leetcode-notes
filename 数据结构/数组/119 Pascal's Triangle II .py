from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def combination(n: int, m: int) -> int:
            """
            :param n choosing m:
            :return: number of choosing
            """
            if m < n // 2:
                return combination(n, n - m)
            ans = 1
            for i in range(n, n - m, -1):
                ans *= i
            for i in range(1, m + 1):
                ans //= i
            return ans

        res = []
        for i in range(rowIndex + 1):
            res.append(combination(rowIndex, i))
        return res
