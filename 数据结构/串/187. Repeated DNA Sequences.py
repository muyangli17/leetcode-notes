from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        record = dict()
        res = []
        l = 0
        r = 10
        length = len(s)
        while r <= length:
            if s[l:r] in record:
                if record[s[l:r]] == 1:
                    res.append(s[l:r])
                    record[s[l:r]] += 1
            else:
                record[s[l:r]] = 1
            l += 1
            r += 1
        return res


s = "AAAAAAAAAAAAA"
solution = Solution()
print(solution.findRepeatedDnaSequences(s=s))
