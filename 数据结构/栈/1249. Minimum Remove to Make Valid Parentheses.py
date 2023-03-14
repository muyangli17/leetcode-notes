class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        leftBracket = 0
        res = ''
        for ch in s:
            if ch == '(':
                leftBracket += 1
                res += ch
            elif ch == ')':
                if leftBracket > 0:
                    leftBracket -= 1
                    res += ch
            else:
                res += ch

        res = ''.join(reversed(res))
        res = res.replace('(', '', leftBracket)
        return ''.join(reversed(res))


s = "(a(b(c)d)"
solution = Solution()
print(solution.minRemoveToMakeValid(s))
