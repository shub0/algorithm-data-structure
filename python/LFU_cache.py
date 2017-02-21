'''
Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?
'''
import collections
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.data = dict()
        self.capacity = capacity
        self.threshold = 0
        self.log = collections.defaultdict(list)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.capacity == 0:
            return -1
        if key in self.data:
            freq = self.increase(key)
            value = self.data[key][0]
            self.data[key] = (value, freq)
            return value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0:
            return
        if key not in self.data:
            self.strip()
        freq = self.increase(key)
        self.data[key] = (value, freq)

    def increase(self, key):
        if key not in self.data:
            self.log[1].append(key)
            self.threshold = 1
            return 1
        else:
            freq = self.data[key][1]
            self.log[freq].remove(key)
            self.log[freq+1].append(key)
            return freq+1

    def strip(self):
        while len(self.data) >= self.capacity:
            if self.log.get(self.threshold, None):
                key = self.log[self.threshold].pop(0)
                del self.data[key]
            else:
                self.threshold += 1

cache = LFUCache( 2 )
print cache.put(1, 1);
print cache.put(2, 2);
print cache.get(1);       # returns 1
print cache.put(3, 3);    # evicts key 2
print cache.get(2);       # returns -1 (not found)
print cache.get(3);       # returns 3.
print cache.put(4, 4);    # evicts key 1.
print cache.get(1);       # returns -1 (not found)
print cache.get(3);       # returns 3
print cache.get(4);       # returns 4
