'''
Design a data structure that supports all following operations in average O(1) time.

Note: Duplicate elements are allowed.
insert(val): Inserts an item val to the collection.
remove(val): Removes an item val from the collection if present.
getRandom: Returns a random element from current collection of elements. The probability of each element being returned is linearly related to the number of same value the collection contains.
Example:

// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();
'''


class RandomizedCollection(object):
    def __init__(self):
        import collections
        self.vals = list()
        self.idxs = collections.defaultdict(set)

    def insert(self, val):
        self.vals.append(val)
        self.idxs[val].add(len(self.vals) - 1)
        return len(self.idxs[val]) == 1

    def remove(self, val):
        if self.idxs[val]:
            out = self.idxs[val].pop()
            ins = self.vals[-1]
            self.vals[out] = ins
            if self.idxs[ins]:
                self.idxs[ins].add(out)
                self.idxs[ins].remove(len(self.vals) - 1)
            self.vals.pop()
            return True
        return False

    def getRandom(self):
        import random
        return random.choice(self.vals)

# Your RandomizedCollection object will be instantiated and called as such:
#["RandomizedCollection","insert","insert","insert","insert","insert","remove","remove","remove","getRandom","getRandom","getRandom","getRandom"]
[[],[0],[1],[2],[3],[3],[2],[3],[0],[],[],[],[]]
obj = RandomizedCollection()
print obj.insert(0)
print obj.insert(1)
print obj.insert(2)
print obj.insert(3)
print obj.insert(3)
print obj.remove(2)
print obj.remove(3)
print obj.remove(0)
print obj.getRandom()
print obj.getRandom()
print obj.getRandom()
print obj.getRandom()

obj2 = RandomizedCollection()
print obj2.insert(1)
print obj2.remove(1)
print obj2.insert(1)
