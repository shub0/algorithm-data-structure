from node_struct import ListNode

'''
Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3

begin to intersect at node c1.
'''

class Solution:
    # @param a ListNode
    # @retrun the size of the linked list
    @classmethod
    def getLength(cls, headA):
        size = 0
        while(headA is not None):
            headA = headA.next
            size += 1
        return size

    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        size_A = Solution.getLength(headA)
        size_B = Solution.getLength(headB)
        if (size_A < size_B):
            return self.getIntersectionNode(headB, headA)
        size_diff = size_A - size_B
        pivotA = headA
        pivotB = headB
        while(size_diff > 0):
            pivotA = pivotA.next
            size_diff -= 1
        
        while(pivotA is not None):
            if (pivotA == pivotB): break
            pivotA = pivotA.next
            pivotB = pivotB.next
        return pivotA
            
if __name__ == '__main__':
    solution = Solution()
    headA = ListNode(1)
    headB = ListNode(2)
    nodeC = ListNode(3)
    headB.next = nodeC
    headA.next = nodeC
    print solution.getIntersectionNode(headA, headB).x
