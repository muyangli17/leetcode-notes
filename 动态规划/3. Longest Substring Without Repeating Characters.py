class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        ans = [1] * len(s)
        for i in range(1, len(s), 1):
            length = 1
            for j in range(i - 1, i - ans[i - 1] - 1, -1):
                if s[j] == s[i]:
                    ans[i] = length
                    break
                else:
                    length += 1
                ans[i] = length

        return max(ans)


s = "pwwkew"
solution = Solution()
print(solution.lengthOfLongestSubstring(s=s))
