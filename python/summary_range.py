'''
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
'''

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        output = list()
        if len(nums) == 0:
            return output
        start = nums[0]
        prev = start
        for num in nums[1:]:
            if num - prev > 1:
                if prev == start:
                    output.append("%d" % start)
                else:
                    output.append( "%d->%d"%(start, prev) )
                start = num
            prev = num
        if prev == start:
            output.append("%d" % start)
        else:
            output.append( "%d->%d"%(start, prev) )
        return output
