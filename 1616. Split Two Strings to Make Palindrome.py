import math


class Solution:
    # 暴力枚举会超时
    # Overtime if enumerates
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def isPalindrome(x: str) -> bool:
            """
            用栈判断x是否为回文字符串（注意下标）
            check whether x is a palindrome (pay attention of the index)
            :param x: input string
            :return: a bool variable
            """
            if x == '':
                return True

            stack = []
            for i in range(len(x) // 2):
                stack.append(x[i])

            for i in range(math.ceil(len(x) / 2), len(x), 1):
                if not x[i] == stack.pop():
                    return False
            return len(stack) == 0

        def isOK(x: str, y: str) -> bool:
            """
            判断当前输入x, y中是否可能包含符合题意的分割
            check whether a valid partition exist for input x, y
            :param x, y: two input string
            :return: a bool variable
            """
            index = 0
            # 试图尽可能多地从x的头部和y的尾部匹配相同字符
            # try to pair the same char from the head of x and the tail of y
            while x[index] == y[-1 - index]:
                index += 1
                # 如果匹配字符超过输入字符串的半长（即符合题意得分割一定存在）
                # if more than half chars are paired (the required partition exists)
                if index >= len(x) // 2:
                    return True
            # 如果匹配字符串数量不足一半（即不确定是否存在分割）
            # 判断 x[index:length - index] 或 y[index:length - index] 是否为回文
            # 如果是，则仍存在符合题意得字符串（在index或length - index处分割）
            # if only less than half chars are paired (the required partition may not exist)
            # check whether x[index:length - index] or y[index:length - index] is a palindrome
            # if yes, then required partition exists (cut it at index or length - index)
            return isPalindrome(x[index:len(x) - index]) or isPalindrome(y[index:len(y) - index])

        # 主函数返回 a为回文 或 b为回文 或 (a, b)符合存在上述划分 或 (b, a)符合存在上述划分
        # return:
        # a is palindrome or b is palindrome or such partition exists in (a, b) or such partition exists in (b, a)
        return isPalindrome(a) or isPalindrome(b) or isOK(a, b) or isOK(b, a)


a = "ulacfd"
b = "jizalu"
solution = Solution()
print(solution.checkPalindromeFormation(a=a, b=b))
