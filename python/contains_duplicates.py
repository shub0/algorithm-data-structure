'''
1.Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

2.Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.

3.Given an array of integers, find out whether there are two distinct indices i and j in the array such that the difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.
'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)

   def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        log = dict()
        for index, num in enumerate(nums):
            if num not in log:
                log[num] = index
            else:
                if index - log[num] <= k:
                    return True
                log[num] = index
        return False

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        log = dict()
        for index, num in enumerate(nums):
            (bucket, offset) = (num/t, 1) if t != 0 else (num, 0)
            for b in range(bucket-offset, bucket+offset+1):
                if b not in log:
                    continue
                if index - log[b][0] <= k and abs(num-log[b][1]) < t:
                    return True
            log[b] = (index, num)
        return False

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        log = dict()
        for index, num in enumerate(nums):
            (b, offset) = (num/t, 1) if t != 0 else (num, 0)
            for bucket in range(b-offset, b+offset+1):
                if bucket not in log:
                    continue
                if abs(index - log[bucket][0]) <= k and abs(num-log[bucket][1]) <= t:
                    return True
            log[b] = (index, num)
        return False

