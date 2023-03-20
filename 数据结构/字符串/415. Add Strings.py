class Solution:
    def addStrings1(self, num1: str, num2: str) -> str:
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

    def addStrings(self, num1: str, num2: str) -> str:
        # ensure num1 is longer
        if len(num1) < len(num2):
            num1 = '0' * (len(num2) - len(num1)) + num1
        else:
            num2 = '0' * (len(num1) - len(num2)) + num2

        listForm = []

        for i in range(- 1, -len(num1) - 1, -1):
            listForm.append(int(num1[i]) + int(num2[i]))

        up = False

        for i in range(len(listForm)):
            listForm[i] += 1 * up
            up = listForm[i] >= 10
            listForm[i] %= 10

        if up:
            listForm.append(1)

        res = ''
        for i in range(-1, -len(listForm) - 1, -1):
            res += str(listForm[i])

        return res


num1 = "1"
num2 = "9"
solution = Solution()
print(solution.addStrings(num1=num1, num2=num2))
