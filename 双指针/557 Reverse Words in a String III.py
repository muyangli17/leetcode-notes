class Solution:
    def reverseWords(self, s: str) -> str:

        ss = list(s)

        start = 0
        for end in range(len(s)):
            if s[end] == ' ':
                (i, j) = (start, end-1)
                while i < j:
                    ss[j] = s[i]
                    ss[i] = s[j]
                    (i, j) = (i + 1, j - 1)
                start = end+1
        (i, j) = (start, len(s) - 1)
        while i < j:
            ss[j] = s[i]
            ss[i] = s[j]
            (i, j) = (i + 1, j - 1)
        return ''.join(ss)


s = "Let's take LeetCode contest"
solution = Solution()
print(solution.reverseWords(s))
