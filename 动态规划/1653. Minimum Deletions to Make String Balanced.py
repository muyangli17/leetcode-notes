class Solution:
    def minimumDeletions1(self, s: str) -> int:
        if len(s) == 1:
            return 0

        aNumFromTail = [0] * (len(s) + 1)
        bNumFromHead = [0] * (len(s) + 1)

        for i in range(0, len(s), 1):
            if s[i] == 'b':
                bNumFromHead[i + 1] = bNumFromHead[i] + 1
            else:
                bNumFromHead[i + 1] = bNumFromHead[i]

        for i in range(len(s), 0, -1):
            if s[i - 1] == 'a':
                aNumFromTail[i - 1] = aNumFromTail[i] + 1
            else:
                aNumFromTail[i - 1] = aNumFromTail[i]

        # print('a:', aNumFromTail)
        # print('b:', bNumFromHead)

        minChange = [0] * (len(s) + 1)
        for i in range(len(minChange)):
            minChange[i] = aNumFromTail[i] + bNumFromHead[i]

        # print('changes:', minChange)

        return min(minChange)

    def minimumDeletions(self, s: str) -> int:
        dp = 0
        countB = 0
        for ch in s:
            if ch == 'a':
                dp = min(dp + 1, countB)
            else:
                countB += 1
        return dp


s = "bbaaaabb"
solution = Solution()
print(solution.minimumDeletions(s=s))
