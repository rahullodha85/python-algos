import collections


class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        if len(self.cache.keys()) > 0:
            if key in self.cache.keys():
                self.cache.move_to_end(key=key)
                return self.cache.get(key)
            else:
                return -1
        else:
            return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache.keys()) > self.size:
            self.cache.popitem(last=False)


testobj = LRUCache(2)

testobj.put(1, 1)
testobj.put(2, 2)
print(testobj.get(1))
