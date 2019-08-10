class Stack(object):

    def __init__(self):
        self.__stack = []

    def get_length(self):
        return self.__stack.__len__()

    def push(self, data):
        self.__stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.__stack.pop(0)

    def is_empty(self):
        return self.get_length() == 0
