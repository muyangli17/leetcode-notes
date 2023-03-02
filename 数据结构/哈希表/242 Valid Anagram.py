class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLetters = dict()
        for char in s:
            if char in sLetters:
                sLetters[char] += 1
            else:
                sLetters[char] = 1

        for char in t:
            if char in sLetters:
                sLetters[char] -= 1
            else:
                return False

        for char in sLetters:
            if sLetters[char] != 0:
                return False
        return True


s = "anagram"
t = "nagaram"

solution = Solution()
print(solution.isAnagram(s=s, t=t))
