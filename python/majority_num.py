'''
1.Given an integer array of size n, find all elements that appear more than floor(n/2) times. The algorithm should run in linear time and in O(1) space.
2.Given an integer array of size n, find all elements that appear more than floor( n/3 ) times. The algorithm should run in linear time and in O(1) space.
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        major = nums[0]
        for num in nums[1:]:
            if num == major:
                count += 1
            else:
                count -= 1
                if count < 0:
                    major = num
                    count = 1
        return major

    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counts = [0, 0]
        things = [0, 0]
        for num in nums:
            if num in things:
                counts[things.index(num)] += 1
            elif 0 in counts:
                things[counts.index(0)] = num
                counts[counts.index(0)] = 1
            else:
                counts[:] = [count - 1 for count in counts]
        return [thing for thing in set(things)
                if nums.count(thing) > len(nums) // 3]

solution = Solution()
print solution.majorityElement2([1,1,1,2,3,4,5,6])
print solution.majorityElement2([1,1,1,2,2,2])
print solution.majorityElement2([2,4,1,1])
