from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        def generateFullRing(n: int) -> List[int]:
            res = [0]
            for i in range(n):
                r = [e + pow(2, i) for e in res]
                r.reverse()
                res = res + r
            return res

        fullRing = generateFullRing(n)

        startIndex = fullRing.index(start)
        return fullRing[startIndex:] + fullRing[:startIndex]


solution = Solution()
print(solution.circularPermutation(n=8, start=85))
