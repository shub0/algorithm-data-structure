'''
Implement a data structure supporting the following operations:

Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".
Challenge: Perform all these in O(1) time complexity.
'''

import collections
import sys
class AllOne(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = collections.defaultdict(int)
        self.freq = collections.defaultdict(set)
        self.max_freq = 0
        self.min_freq = 1

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        orig = self.data[key]
        if (key in self.freq[self.min_freq]) and (len(self.freq[self.min_freq]) == 1):
            self.min_freq += 1
        else:
            self.min_freq = max(1, min(self.min_freq, orig+1))
        if orig > 0:
            self.freq[orig].remove(key)
        self.freq[orig+1].add(key)
        self.data[key] += 1
        self.max_freq = max(self.max_freq, orig+1)

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        orig = self.data[key]
        if orig == 0:
            return
        if (key in self.freq[self.max_freq]) and (len(self.freq[self.max_freq]) == 1):
            self.max_freq -= 1
        else:
            self.max_freq = max(self.max_freq, orig-1)
        self.freq[orig].remove(key)
        self.data[key] -= 1
        self.freq[orig-1].add(key)
        self.min_freq = max(1, min(self.min_freq, orig-1))

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if not self.freq[self.max_freq]:
            return ""
        key = self.freq[self.max_freq].pop()
        self.freq[self.max_freq].add(key)
        return key

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if not self.freq[self.min_freq]:
            return ""
        key = self.freq[self.min_freq].pop()
        self.freq[self.min_freq].add(key)
        return key

# Your AllOne object will be instantiated and called as such:
obj = AllOne()
obj.inc("Dumbo")
obj.inc("Dumbo")
obj.inc("BB")
print obj.getMaxKey()
print obj.getMinKey()
obj.dec("Dumbo")
obj.dec("Dumbo")
print obj.getMaxKey()
print obj.getMinKey()
