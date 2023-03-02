def isBadVersion(m):
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(1):
            return 1
        i = 1
        j = n
        while j - i > 1:
            m = i + (j - i) // 2
            if isBadVersion(m):
                j = m
            else:
                i = m
        return j
