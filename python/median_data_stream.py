'''
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
'''
import heapq
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # ideally should be implemented as a self-balanced binary search tree, eg RBT
        self.left_heap = [] # left tree of self-balance tree, max_heap
        self.right_heap = [] # right tree of self-balance tree, min_heap

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if len(self.left_heap) == 0:
            heapq.heappush(self.left_heap, -num)
        else:
            top = self.left_heap[0]
            if num > -top:
                # push to right tree
                heapq.heappush(self.right_heap, num)
            else:
                # push to left tree
                heapq.heappush(self.left_heap, -num)
            # re-balance
            while (len(self.right_heap) - len(self.left_heap) > 1):
                top = heapq.heappop(self.right_heap)
                heapq.heappush(self.left_heap, -top)
            while (len(self.left_heap) - len(self.right_heap) > 1):
                top = heapq.heappop(self.left_heap)
                heapq.heappush(self.right_heap, -top)

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        left_size = len(self.left_heap)
        right_size = len(self.right_heap)
        left_val = -self.left_heap[0] if left_size > 0 else 0
        right_val = self.right_heap[0] if right_size > 0 else 0
        if (left_size + right_size) % 2 == 0:
            return 0.5 * (left_val + right_val)
        elif left_size > right_size:
            return left_val
        else:
            return right_val


# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
mf.addNum(2)
mf.addNum(3)
print mf.findMedian()

