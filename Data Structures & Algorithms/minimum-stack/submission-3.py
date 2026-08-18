class MinStack:

    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, val: int) -> None:
        if not self.min_stack or self.min_stack[-1] >= val:
            self.min_stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if self.min_stack[-1] == popped:
            self.min_stack.pop()
        return popped

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
