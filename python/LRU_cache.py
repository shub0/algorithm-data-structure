#! /usr/bin/python

'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
'''

class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        import collections
        self.capacity = capacity
        self.used = 0
        self.cache = dict()
        self.count = collections.defaultdict(int)
        self.log = list()

    def update_log(self, key):
        self.count[key] += 1
        self.log.append(key)

    def strip(self):
        while self.used > self.capacity:
            key = self.log.pop(0)
            self.count[key] -= 1
            if self.count[key] == 0:
                self.used -= 1
                del self.cache[key]

    # @return an integer
    def get(self, key):
        if key not in self.cache:
            return -1
        self.update_log(key)
        return self.cache[key]

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value, size=1):
        if key not in self.cache:
            self.used += size
        self.cache[key] = value
        self.update_log(key)
        self.strip()

import collections
class LRUCache2(collections.OrderedDict):

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        super(LRUCache2, self).__init__()

    # @return an integer
    def get(self, key):
        if key in self:
            self[key] = self[key]
            return self[key]
        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(0)

    def __setitem__(self, key, value):
        if key in self:
            del self[key]
        collections.OrderedDict.__setitem__(self, key, value)

if __name__ == '__main__':
    my_cache = LRUCache(2)
    my_cache.set(2,1)
    my_cache.set(1,1)
    print my_cache.get(2)
    my_cache.set(4,1)
    print my_cache.get(1)
    print my_cache.get(2)
