'''
The following code implmented two use cases using segment tree
1. Range sum, which could be done by Binary Index Tree
2. Range Minimun Query(RMQ)

Time Complexity for tree construction is O(n). There are total 2n-1 nodes, and value of every node is calculated only once in tree construction.
Time complexity to query is O(Logn). To query a sum, we process at most four nodes at every level and number of levels is O(Logn).
The time complexity of update is also O(Logn). To update a leaf value, we process one node at every level and number of levels is O(Logn).
'''

class SegmentTree(object):
    def __init__(self, num):
        self.size = len(num)
        self.num = num
        tree_size = 2 * self.size + 1
        self.tree = [0] * tree_size
        self.constructUtil(num, 0, self.size - 1, 0)

    def constructUtil(self, num, start, end, index):
        if (start == end):
            self.tree[index] = num[start]
            return num[start]

        mid = (start + end) / 2
        self.tree[index] = (self.constructUtil(num, start, mid, index*2+1)+
                        self.constructUtil(num, mid+1, end, index*2+2))
        return self.tree[index]

    def getSum(self, start, end):
        # Check for erroneous input values
        if (start < 0 or end > self.size - 1 or start > end):
            raise ValueError()
        return self.getSumUtil(0, self.size - 1, start, end, 0);

    def getSumUtil(self, search_start, search_end, query_start, query_end, index):
        if (query_start <= search_start and query_end >= search_end):
            return self.tree[index]

        if (search_end < query_start or search_start > query_end):
            return 0

        mid = (search_start+search_end) / 2
        return (self.getSumUtil(search_start, mid, query_start, query_end, 2*index+1)+
                self.getSumUtil(mid+1, search_end, query_start, query_end, 2*index+2))

    def updateValue(self, index, new_value):
        if (index < 0) or (index > self.size):
            raise ValueError()
        diff = new_value - self.num[index]
        self.num[index] = new_value
        self.updateValueUtil(0, self.size-1, 0, index, diff)

    def updateValueUtil(self, start, end, pos, index, diff):
        if (index < start) or (index > end):
            return
        self.tree[pos] += diff
        if (start < end):
            mid = (end - start) / 2 + start
            self.updateValueUtil(start, mid, 2*pos+1, index, diff)
            self.updateValueUtil(mid+1, end, 2*pos+2, index, diff)

class RMQ(object):
    def __init__(self, num):
        self.size = len(num)
        self.num = num
        tree_size = 2 * self.size + 1
        self.tree = [0] * tree_size
        self.constructUtil(num, 0, self.size - 1, 0)

    def constructUtil(self, num, start, end, index):
        if (start == end):
            self.tree[index] = num[start]
            return num[start]

        mid = (start + end) / 2
        self.tree[index] = (self.constructUtil(num, start, mid, index*2+1)+
                        self.constructUtil(num, mid+1, end, index*2+2))
        return self.tree[index]

    def getSum(self, start, end):
        # Check for erroneous input values
        if (start < 0 or end > self.size - 1 or start > end):
            raise ValueError()
        return self.getSumUtil(0, self.size - 1, start, end, 0);

    def getSumUtil(self, search_start, search_end, query_start, query_end, index):
        if (query_start <= search_start and query_end >= search_end):
            return self.tree[index]

        if (search_end < query_start or search_start > query_end):
            return 0

        mid = (search_start+search_end) / 2
        return (self.getSumUtil(search_start, mid, query_start, query_end, 2*index+1)+
                self.getSumUtil(mid+1, search_end, query_start, query_end, 2*index+2))

    def updateValue(self, index, new_value):
        if (index < 0) or (index > self.size):
            raise ValueError()
        diff = new_value - self.num[index]
        self.num[index] = new_value
        self.updateValueUtil(0, self.size-1, 0, index, diff)

    def updateValueUtil(self, start, end, pos, index, diff):
        if (index < start) or (index > end):
            return
        self.tree[pos] += diff
        if (start < end):
            mid = (end - start) / 2 + start
            self.updateValueUtil(start, mid, 2*pos+1, index, diff)
            self.updateValueUtil(mid+1, end, 2*pos+2, index, diff)


class RMQ(object):
    def __init__(self, num):
        self.size = len(num)
        self.num = num
        tree_size = 2*self.size + 1
        self.tree = [float("inf")] * tree_size
        self.constructUtil(num, 0, self.size-1, 0)

    def constructUtil(self, num, start, end, index):
        if (start == end):
            self.tree[index] = num[start]
            return num[start]

        mid = (end-start) / 2 + start
        self.tree[index] = min( self.constructUtil(num, start, mid, 2*index+1), self.constructUtil(num, mid+1, end, 2*index+2) )
        return self.tree[index]

    def getMin(self, start, end):
        if (start < 0 or end > self.size-1 or start > end):
            raise ValueError()
        return self.getMinUtil(0, self.size-1, start, end, 0)

    def getMinUtil(self, search_start, search_end, query_start, query_end, index):
        if (query_start <= search_start and query_end >= search_end):
            return self.tree[index]

        if (search_end < query_start or search_start > query_end):
            return float("inf")

        mid = (search_end - search_start) / 2 + search_start
        return min( self.getMinUtil(search_start, mid, query_start, query_end, 2*index+1), self.getMinUtil(mid+1, search_end, query_start, query_end, 2*index+2) )


tree = SegmentTree([0,1,2,3,4,5])
print ("Expected 6, got %d" % tree.getSum(0,3))
tree.updateValue(0, 3)
print ("Expected 9, got %d" % tree.getSum(0,3))

rmq = RMQ([6,1,4,7,9,5])
print ("Expected 4, got %d" % rmq.getMin(2,4))
