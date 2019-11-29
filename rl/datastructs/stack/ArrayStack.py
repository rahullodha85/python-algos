class Stack(object):

    def __init__(self):
        self.__stack = []

    def get_length(self):
        return self.__stack.__len__()

    def push(self, data):
        self.__stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.__stack.pop(self.__stack.__len__() - 1)

    def is_empty(self):
        return self.get_length() == 0

    def peek(self):
        if not self.is_empty():
            return self.__stack[self.__stack.__len__() - 1]
