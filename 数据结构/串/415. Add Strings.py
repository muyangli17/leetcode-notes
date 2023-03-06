class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # ensure num1 is longer
        if len(num1) < len(num2):
            (num1, num2) = (num2, num1)

        res = ''
        up = False

        for i in range(- 1, -len(num2) - 1, -1):
            ans = int(num1[i]) + int(num2[i])
            if up:
                ans += 1
            digit = str(ans % 10)
            up = (ans // 10 == 1)

            res = digit + res

        if len(num1) == len(num2):
            if up:
                return '1' + res

        index = -len(num2) - 1
        while index >= -len(num1):
            if up:
                if num1[index] == '9':
                    res = '0' + res
                else:
                    res = str(int(num1[index]) + 1) + res
                    up = False
            else:
                res = num1[index] + res
            index -= 1

        if up:
            res = '1' + res

        return res


num1 = "923"
num2 = "111"
solution = Solution()
print(solution.addStrings(num1=num1, num2=num2))
