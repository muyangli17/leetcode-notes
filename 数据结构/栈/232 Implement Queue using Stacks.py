class MyQueue:

    def __init__(self):
        self.firstStack = []
        self.secondStack = []

    def push(self, x: int) -> None:
        self.firstStack.append(x)

    def pop(self) -> int:
        while len(self.firstStack) > 1:
            self.secondStack.append(self.firstStack.pop())

        res = self.firstStack.pop()

        while len(self.secondStack) > 0:
            self.firstStack.append(self.secondStack.pop())
        return res

    def peek(self) -> int:
        while len(self.firstStack) > 1:
            self.secondStack.append(self.firstStack.pop())

        res = self.firstStack[-1]

        while len(self.secondStack) > 0:
            self.firstStack.append(self.secondStack.pop())
        return res

    def empty(self) -> bool:
        return self.firstStack == []

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
