class Solution:
    def longestPalindrome(self, s: str) -> int:
        record = dict()
        for char in s:
            if char not in record:
                record[char] = 1
            else:
                record[char] += 1

        res = 0
        containOdd = False
        for key in record:
            if record[key] % 2 == 0:
                res += record[key]
            else:
                res += (record[key] - 1)
                containOdd = True

        if containOdd:
            res += 1

        return res


s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemld" \
    "oftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnatio" \
    "nmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecann" \
    "othallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractT" \
    "gheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathe" \
    "rtobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobehereded" \
    "icatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygav" \
    "ethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGods" \
    "hallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
solution = Solution()
print(solution.longestPalindrome(s=s))
