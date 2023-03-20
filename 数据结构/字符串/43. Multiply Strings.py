class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def addStrings(num1: str, num2: str) -> str:
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

        ans = '0'

        for index2 in range(-1, -len(num2) - 1, -1):
            middleAns = '0'
            for index1 in range(-1, -len(num1) - 1, -1):
                pow10 = -index1 - index2 - 2
                middleAns = addStrings(middleAns, str(int(num1[index1]) * int(num2[index2]) * (10 ** pow10)))
            ans = addStrings(ans, middleAns)

        return ans


num1 = "123"
num2 = "456"
solution = Solution()
print(solution.multiply(num1=num1, num2=num2))
