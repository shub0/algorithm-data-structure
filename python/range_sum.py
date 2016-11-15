'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
'''

class NumArray(object):
    def __init__(self, array):
        self.size = len(array)
        self.tree = [0] * (self.size)
        for (index, num) in enumerate(array):
            self.increment(index, num)

    # Check pre-fix sum up to index (inclusive)
    def readSum(self, index):
        range_sum = 0
        # convert to 1 based to fast search
        index += 1
        while (index > 0):
            range_sum += self.tree[index-1]
            # top down
            index -= ( index & -index)
        return range_sum

    # Check range sum from start to end (both inclusive)
    def sumRange(self, start, end):
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
            # bottom up
            index += (index & (-index))


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)
