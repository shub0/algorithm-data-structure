'''
The implementation of binary indexed tree in 1D.
Binary Index Tree(BIT) could solve mutable prefix sum problem in log(N) time and update array operation in log(N) time.
The tree building takes O(NlogN) time with additional O(N) space.
Similary algorithm could be easily extended to 2D array as well.
'''


class BinaryIndexTree(object):
    def __init__(self, array):
        self.size = len(array)
        self.tree = [0] * (self.size)
        for (index, num) in enumerate(array):
            self.increment(index, num)

    # Check pre-fix sum up to index (inclusive)
    def readSum(self, index):
        sum = 0
        # convert to 1 based to fast search
        index += 1
        while (index > 0):
            sum += self.tree[index-1]
            index -= ( index & -index)
        return sum

    # Check range sum from start to end (both inclusive)
    def readRangeSum(self, start, end):
        return self.readSum(end) if start == 0 else self.readSum(end) - self.readSum(start-1)

    def readElement(self, index):
        if index == 0:
            return self.readSum(0)
        return self.readSum(index) - self.readSum(index-1)

    def update(self, index, value):
        orig_value = self.readElement(index)
        incr = value - orig_value
        self.increment(index, incr)

    def increment(self, index, incr):
        # convert to 1 based to fast search
        index += 1
        while (index <= self.size):
            self.tree[index-1] += incr
            index += (index & (-index))

bit = BinaryIndexTree([1,0,2,1,1,3,0,4,2,5,2,2,3,1,0,2])
print ("Expected 1, got %d" % bit.readSum(0))
print ("Expected 4, got %d" % bit.readSum(3))
print ("Expected 7, got %d" % bit.readRangeSum(1,5))
print ("Expected 0, got %d" % bit.readElement(1))
bit.update(1, 3)
print ("Expected 7, got %d" % bit.readSum(3))
