'''
Implement a data structure supporting the following operations:

Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".
Challenge: Perform all these in O(1) time complexity.
'''

# Double Linked List Node
class Node:
    def __init__(self, value, next, prev, key):
        self.next = next
        self.prev = prev
        self.value = value
        self.keys = {key}

class DoubleList:
    def __init__(self):
        self.head = Node(-1, None, None, "")
        self.tail = Node(-1, None, None, "")
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertAfter(self, node, val, key):
        new = Node(val, node.next, node, key)
        node.next = new
        new.next.prev = new
        return new

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del node

class AllOne(object):

    def __init__(self):
        self.dll = DoubleList()
        self.data = {}

    def inc(self, key):
        if key not in self.data:
            n = self.dll.insertAfter(self.dll.head, 0, key)
            self.data[key] = n
        else:
            n = self.data[key]

        if n.value + 1 == n.next.value:
            # merge with next
            self.data[key] = n.next
            n.keys.remove(key)
            n.next.keys.add(key)
        elif len(n.keys) == 1:
            # increment in place
            n.value += 1
        else:
            # insert new node
            new = self.dll.insertAfter(n, n.value+1, key)
            self.data[key] = new
            n.keys.remove(key)

        #Garbage collection
        if len(n.keys) <= 0:
            self.dll.remove(n)

    def dec(self, key):
        if key not in self.data:
            return
        else:
            n = self.data[key]

        if n.value == 1:
            # remove key/node
            del self.data[key]
            n.keys.remove(key)
        elif n.value - 1 == n.prev.value:
            # merge with previous
            self.data[key] = n.prev
            n.keys.remove(key)
            n.prev.keys.add(key)
        elif len(n.keys) == 1:
            # decrement in place
            n.value -= 1
        else:
            # insert new node
            new = self.dll.insertAfter(n.prev, n.value-1, key)
            n.keys.remove(key)
            self.data[key] = new

        # Garbage collection
        if len(n.keys) <= 0:
            self.dll.remove(n)

    def getMaxKey(self):
        if self.dll.head.next.value == -1:
            return ""
        for k in self.dll.tail.prev.keys:
            break
        return k

    def getMinKey(self):
        if self.dll.head.next.value == -1:
            return ""
        for k in self.dll.head.next.keys:
            break
        return k

# Your AllOne object will be instantiated and called as such:
'''
["inc","inc","inc","inc","inc","inc","dec","dec","getMinKey","dec","getMaxKey","getMinKey"]
[["a"],["b"],["b"],["c"],["c"],["c"],["b"],["b"],[],["a"],[],[]]
'''

obj = AllOne()
obj.inc("a")
obj.inc("b")
obj.inc("b")
obj.inc("c")
obj.inc("c")
obj.inc("c")
obj.dec("b")
obj.dec("b")
print obj.min_freq
print obj.freq[obj.min_freq]
obj.dec("a")
print obj.max_freq
print obj.freq[obj.max_freq]
print obj.min_freq
print obj.freq[obj.min_freq]


