#! /usr/bin/python

'''
Given an array of integers, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution.
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        _num  = sorted(num)
        left  = 0
        right = len(num) - 1
        while left < right:
            sum = _num[left] + _num[right]
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                break
        index1 = num.index(_num[left])
        index2 = 0
        for index in range(len(num)):
            if num[index] == _num[right] and index != index1:
                index2 = index
                break
        index1 += 1
        index2 += 1
        return (index1, index2) if index1 < index2 else (index2, index1)

if __name__ == '__main__':
    solution = Solution()
    print solution.twoSum([2,7,11,15], 9)
