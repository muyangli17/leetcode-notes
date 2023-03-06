class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        splitted = s.split(' ')

        if len(pattern) != len(splitted):
            return False

        patternHash = dict()
        sHash = dict()
        for i in range(len(pattern)):
            ch = pattern[i]
            word = splitted[i]

            if ch not in patternHash and word not in sHash:
                patternHash[ch] = word
                sHash[word] = ch
            elif ch in patternHash and word in sHash:
                if patternHash[ch] != word or sHash[word] != ch:
                    return False
            else:
                return False

        return True


pattern = "abba"
s = "dog dog dog dog"
solution = Solution()
print(solution.wordPattern(pattern=pattern, s=s))
