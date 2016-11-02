'''
Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i <= j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:
Given nums = [-2, 5, -1], lower = -2, upper = 2,
Return 3.
The three ranges are : [0, 0], [2, 2], [0, 2] and their respective sums are: -2, -1, 2.
'''

class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        sums = [0]
        for num in nums:
            sums.append(sums[-1] + num)
        return self.countMergeSort(sums, 0, len(sums), lower, upper)

    def countMergeSort(self, sums, start, end, lower, upper):
        if (end - start) <= 1:
            return 0
        mid = (end + start) / 2
        count = self.countMergeSort(sums, start, mid, lower, upper) + \
                self.countMergeSort(sums, mid, end, lower, upper)
        j, k, t = mid, mid, mid
        cache = list()
        for i in range(start, mid):
            while (k < end and sums[k] - sums[i] < lower):
                k += 1
            while (j < end and sums[j] - sums[i] <= upper):
                j += 1
            while (t < end and sums[t] < sums[i]):
                cache.append(sums[t])
                t += 1
            cache.append(sums[i])
            count += (j - k)
        for num in cache:
            sums[start] = num
            start += 1
        return count

solution = Solution()
print solution.countRangeSum([-2,5,-1], -2,2)
