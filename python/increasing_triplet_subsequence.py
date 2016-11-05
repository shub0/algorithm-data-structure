"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 <= i < j < k < n else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.
"""

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import sys
        size = len(nums)
        aux = [sys.maxint, sys.maxint]
        for num in nums:
            if num <= aux[0]:
                aux[0] = num
            elif num <= aux[1]:
                aux[1] = num
            else:
                return True
        return False

solution = Solution()
print solution.increasingTriplet([5,4,3,2,1])
print solution.increasingTriplet([4,3,5,2,1,6])
print solution.increasingTriplet([5,6,2,3,4,5])
