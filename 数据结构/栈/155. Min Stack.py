'''
class MinStack:

    def __init__(self):
        self.stack = []
        self.ordered = []

    def searchInsert(self, target: int) -> int:
        i = 0
        j = len(self.ordered) - 1
        while i <= j:
            m = i + (j - i) // 2
            if target == self.ordered[m]:
                return m
            if target < self.ordered[m]:
                j = m - 1
            if target > self.ordered[m]:
                i = m + 1
        return i

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.ordered.insert(self.searchInsert(val), val)

    def pop(self) -> None:
        self.ordered.remove(self.stack.pop())

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.ordered[0]
'''


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(val)
            self.stack.append(val)
        else:
            if val <= self.stack[-2]:
                self.stack.append(val)
                self.stack.append(val)
            else:
                self.stack.append(self.stack[-2])
                self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[-2]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

mStack = MinStack()
print(mStack.push(-2))
print(mStack.push(0))
print(mStack.push(-3))
print(mStack.getMin())
print(mStack.pop())
print(mStack.top())
print(mStack.getMin())
