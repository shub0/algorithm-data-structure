"""
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Examples:
Input: [1,7,4,9,2,5]
Output: 6
The entire sequence is a wiggle sequence.

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].

Input: [1,2,3,4,5,6,7,8,9]
Output: 2

Follow up:
Can you do it in O(n) time?
"""

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        max_dir = [None] * size
        max_size = [1] * size
        if size < 2:
            return size
        flag = True
        for index in range(1, size):
            _size = max([0] + [ max_size[idx] for idx in range(1, index) if (nums[index] > nums[idx] and not max_dir[idx]) or (nums[index] < nums[idx] and max_dir[idx]) ])
            if nums[index] != nums[0]:
                _size = max(1, _size)
            if _size == 1:
                max_dir[index] = (nums[index] > nums[0])
                max_size[index] = 1+_size
            elif _size > 1:
                idx = max_size.index(_size)
                max_dir[index] = (not max_dir[idx])
                max_size[index] = 1+_size
        return max(max_size)

solution = Solution()
print solution.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])
print solution.wiggleMaxLength([1,2,3,4,5,6,7,8,9])
print solution.wiggleMaxLength([1,7,4,9,2,5])
print solution.wiggleMaxLength([0,0])
