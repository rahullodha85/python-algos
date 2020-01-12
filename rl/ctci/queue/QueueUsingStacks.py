from rl.ctci.stack.Stack import Stack


class QueueUsingStacks:

    def __init__(self):
        self.newest_stack = Stack()
        self.oldest_stack = Stack()

    def add(self, data):
        self.newest_stack.push(data)

    def peek(self):
        self.shift_stacks()
        return self.oldest_stack.peek()

    def remove(self):
        self.shift_stacks()
        return self.oldest_stack.pop()

    def shift_stacks(self):
        if self.oldest_stack.is_empty():
            while not self.newest_stack.is_empty():
                self.oldest_stack.push(self.newest_stack.pop())