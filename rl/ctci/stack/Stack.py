class Stack:
    class StackNode:
        
        def __init__(self, data):
            self.data = data
            self.next = None
        
    def __init__(self):
        self.top: self.StackNode = None
    
    def pop(self):
        if self.top:
            data = self.top.data
            self.top = self.top.next
            return data
        else:
            raise Exception()
    
    def push(self, data):
        top = self.StackNode(data)
        top.next = self.top
        self.top = top
    
    def peek(self):
        if not self.top:
            raise Exception()
        return self.top.data
    
    def is_empty(self):
        return self.top is None

test = Stack()
test.push(1)
print(test.is_empty())
print(test.peek())
print(test.pop())
print(test.is_empty())