class MinStack:

    def __init__(self):
        self.stack = list()
        self.min_stack = list()

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.min_stack) < 1:
            self.min_stack.append(x)
        else:
            if x <= self.getMin():
                self.min_stack.append(x)

    def pop(self) -> None:
        if self.top() == self.getMin():
            self.min_stack.pop(len(self.min_stack)-1)
        self.stack.pop(len(self.stack) - 1)

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        if len(self.min_stack) > 0:
            return self.min_stack[len(self.min_stack) - 1]