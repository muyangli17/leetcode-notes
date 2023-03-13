from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        startPos = dict()
        endPos = dict()

        for i in range(len(s)):
            ch = s[i]
            if ch not in startPos:
                startPos[ch] = i
                endPos[ch] = i
            else:
                endPos[ch] = i

        res = []

        intervalStart = 0
        intervalEnd = -1
        while intervalEnd < len(s) - 1:
            index = intervalStart
            intervalEnd = endPos[s[index]]
            while index < intervalEnd:
                containedCh = s[index]
                intervalEnd = max(intervalEnd, endPos[containedCh])
                index += 1
            res.append(intervalEnd - intervalStart + 1)
            intervalStart = intervalEnd + 1

        return res


s = "ababcbacadefegdehijhklij"
solution = Solution()
print(solution.partitionLabels(s=s))
