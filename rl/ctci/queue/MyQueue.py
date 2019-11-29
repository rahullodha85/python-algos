class MyQueue:

    class __QueueNode:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.first: self.__QueueNode = None
        self.last: self.__QueueNode = None

    def is_empty(self):
        return self.first is None

    def peek(self):
        if self.is_empty():
            raise Exception()
        return self.first.data

    def add(self, data):
        node = self.__QueueNode(data)

        if self.last:
            self.last.next = node
        self.last = node
        if not self.first:
            self.first = self.last

    def remove(self):
        if not self.first:
            raise Exception()
        data = self.first.data
        self.first = self.first.next
        if not self.first:
            self.last = None
        return data


test = MyQueue()
print(test.is_empty())
test.add(2)
print(test.is_empty())
print(test.peek())
test.add(3)
print('First: {}'.format(test.first.data))
print('Last: {}'.format(test.last.data))
test.add(4)
print('First: {}'.format(test.first.data))
print('Last: {}'.format(test.last.data))
print(test.remove())
print(test.remove())
print(test.remove())
print(test.is_empty())