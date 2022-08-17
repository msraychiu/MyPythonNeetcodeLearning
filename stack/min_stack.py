class MinStack:

    def __init__(self):
        self.stack = []
        self.minvalue = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minvalue is None or val < self.minvalue:
            self.minvalue = val

    def pop(self) -> None:
        popitem = self.stack.pop()
        if len(self.stack) > 0 and popitem == self.minvalue:
            self.minvalue = min(self.stack)
        elif len(self.stack) == 0:
            self.minvalue = None

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.minvalue

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()