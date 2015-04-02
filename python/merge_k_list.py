#! /usr/bin/python

'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''

from node_struct import ListNode

# Assume the average length of each list are n and k lists total
# The solution requires an additional heap with size K
# Initialize heap requires O(K)
# Every iteration heappush requires O(logK) and heappop requires O(1), therefore total is O(N) * [O(logK) + O(1)] is O(NlogK) + O(K) + O(N)

class Solution:
    
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        import heapq
        k = len(lists)
        pivot = ListNode(0)
        cursor = pivot
        nodes  = list()
        for index in range(k):
            if lists[index]:
                heapq.heappush(nodes,(lists[index].x, index))
        while len(nodes) > 0:
            min_node = heapq.heappop(nodes)
            index = min_node[1]
            cursor.next = lists[index]
            lists[index] = lists[index].next
            if lists[index]:
                heapq.heappush(nodes, (lists[index].x, index))
            cursor = cursor.next
        return pivot.next

if __name__ == '__main__':
    a = ListNode(0)
    a.next = ListNode(3)
    a.next.next = ListNode(3)

    b = ListNode(1)
    b.next = ListNode(4)
    c = ListNode(2)
    c.next = ListNode(5)
    solution = Solution()
    d = solution.mergeKLists([a,b,c,])
    while d:
        print d.x
        d = d.next
