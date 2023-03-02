class Solution:
    def isValid1(self, s: str) -> bool:
        stack = []
        for ch in s:
            if (ch == '(') or (ch == '[') or (ch == '{'):
                stack.append(ch)
            if ch == ')':
                if len(stack) == 0:
                    return False
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            if ch == ']':
                if len(stack) == 0:
                    return False
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            if ch == '}':
                if len(stack) == 0:
                    return False
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

    def isValid2(self, s: str) -> bool:
        while '{}' in s or '[]' in s or '()' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''


solution = Solution()
print(solution.isValid('()(){}[]'))
