from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def fingerprint(s: str) -> str:
            l = list(s)
            l.sort()
            return str(l)

        record = dict()
        res = []

        for word in strs:
            fpt = fingerprint(word)
            if fpt in record:
                res[record[fpt]].append(word)
            else:
                record[fpt] = len(res)
                res.append([word])

        return res


# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# strs = [""]
strs = ["a"]
solution = Solution()
print(solution.groupAnagrams(strs))
