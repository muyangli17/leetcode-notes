import math


class Solution:
    def longestPalindrome(self, s: str) -> str:
        F = [1] * len(s)
        palindromeStr = s[0]

        def isPalindrome(toCheck: str) -> bool:
            L = len(toCheck)
            stack = []
            for i in range(L // 2):
                stack.append(toCheck[i])

            for i in range(math.ceil(L / 2), L):
                if not toCheck[i] == stack.pop():
                    return False
            return True

        for n in range(1, len(s)):
            if n >= 2 and isPalindrome(s[n - 1 - F[n - 2]:n + 1]):
                F[n] = F[n - 2] + 2
                palindromeStr = s[n - F[n - 2] - 1:n + 1]
            elif isPalindrome(s[n - F[n - 1]:n + 1]):
                F[n] = F[n - 1] + 1
                palindromeStr = s[n - F[n - 1]:n + 1]
            else:
                F[n] = F[n - 1]

        return palindromeStr
        # return F[-1]


solution = Solution()
print(solution.longestPalindrome('abcba'))
