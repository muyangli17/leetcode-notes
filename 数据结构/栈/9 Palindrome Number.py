import math


class Solution:
    def isPalindrome1(self, x: int) -> bool:
        # 有人提供了测试数据‘1122’把这个算法卡掉了
        # 测试数据位置115509/11510
        # 震撼亲妈一整年
        s = str(x)
        if len(s) % 2 == 1:
            s = s.replace(s[len(s) // 2], '', 1)

        while '11' in s or '22' in s or '33' in s or '44' in s or '55' in s or '66' in s or '77' in s or '88' in s or '99' in s or '00' in s:
            s = s.replace('11', '')
            s = s.replace('22', '')
            s = s.replace('33', '')
            s = s.replace('44', '')
            s = s.replace('55', '')
            s = s.replace('66', '')
            s = s.replace('77', '')
            s = s.replace('88', '')
            s = s.replace('99', '')
            s = s.replace('00', '')
        return s == ''

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True

        digitsnum = math.floor(math.log10(x)) + 1
        stack = []
        for i in range(digitsnum // 2):
            stack.append(x % 10)
            x = x // 10

        if digitsnum % 2 == 1:
            x = x // 10

        for i in range(digitsnum // 2):
            if not x % 10 == stack[-1]:
                return False
            stack.pop()
            x = x // 10
        return len(stack) == 0


solution = Solution()
print(solution.isPalindrome(10))
