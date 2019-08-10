class Stack(object):

    def __init__(self):
        self.__stack = []

    def get_length(self):
        return self.__stack.__len__()
