class Solution:

    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        # DFS遍历所有可能情况。考虑数据规模len(s)<100，总可能情况不超过10 * 10 * 100 = 1e4种
        # DFS for all possible situation. Given len(s)<100, number of all possible string <= 10000 = 1e4
        def aOpt(s: str, a: int) -> str:
            next = ""
            for i in range(len(s)):
                if i % 2 == 0:
                    next = next + s[i]
                else:
                    next = next + str((int(s[i]) + a) % 10)
            return next

        def bOpt(s: str, b: int) -> str:
            next = s[-b:] + s[:-b]
            return next

        smallest = s
        toCheck = [s]
        record = {s: True}
        while len(toCheck) > 0:
            search = toCheck.pop(0)
            smallest = min(search, smallest)

            nextA = aOpt(s=search, a=a)
            if nextA not in record:
                record[nextA] = True
                toCheck.append(nextA)

            nextB = bOpt(s=search, b=b)
            if nextB not in record:
                record[nextB] = True
                toCheck.append(nextB)

        return smallest


s = "43987654"
a = 7
b = 3

solution = Solution()
print(solution.findLexSmallestString(s=s, a=a, b=b))
