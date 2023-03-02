class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        allLetters = dict()
        for char in magazine:
            if char in allLetters:
                allLetters[char] += 1
            else:
                allLetters[char] = 1

        for char in ransomNote:
            if not char in allLetters:
                return False
            elif allLetters[char] == 0:
                return False
            else:
                allLetters[char] -= 1
        return True


ransomNote = "aa"
magazine = "ab"

solution = Solution()
print(solution.canConstruct(ransomNote=ransomNote, magazine=magazine))
