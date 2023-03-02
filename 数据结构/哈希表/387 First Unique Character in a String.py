class Solution:
    def firstUniqChar(self, s: str) -> int:
        recording = dict()
        for char in s:
            if not char in recording:
                recording[char] = 1
            else:
                recording[char] += 1

        for index in range(len(s)):
            if recording[s[index]] == 1:
                return index
        return -1


s = "loveleetcode"

solution = Solution()
print(solution.firstUniqChar(s=s))
