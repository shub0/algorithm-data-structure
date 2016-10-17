'''
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].
'''
class Tree(object):
    def __init__(self, val):
        self.val = val
        self.size = 1
        self.left = None
        self.right = None

    def insert(self, val):
        self.size += 1
        if self.val <= val:
            if self.right:
                self.right.insert(val)
            else:
                self.right = Tree(val)
        else:
            if self.left:
                self.left.insert(val)
            else:
                self.left = Tree(val)

    def search(self, val, index = 0):
        if val == self.val:
            left_size = self.left.size if self.left else 0
            return index + left_size
        elif val < self.val and self.left:
            return self.left.search(val, index)
        elif val > self.val and self.right:
            left_size = self.left.size if self.left else 0
            return self.right.search(val, left_size+index+1)
        else:
            return -1

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        MAX_INT = 2e10
        bst = Tree(MAX_INT)
        for num in nums[::-1]:
            bst.insert(num)
            pos = bst.search(num)
            output.append(pos)
        return output[::-1]

solution = Solution()
print "expected [3, 2, 2, 1, 1, 0], got"
print solution.countSmaller([5,2,6,1,8,0])
