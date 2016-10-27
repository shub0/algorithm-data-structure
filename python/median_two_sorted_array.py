#! /usr/bin/python

'''
There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
'''

class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        if (m + n) % 2 == 0:
            return 0.5 * self.findKth(nums1, nums2, (m+n) / 2 + 1) + 0.5 * self.findKth(nums1, nums2, (m+n) / 2)
        else:
            return self.findKth(nums1, nums2, (m+n) / 2 + 1)

    def findKth(self, nums1, nums2, k):
        if len(nums1) > len(nums2):
            return self.findKth(nums2, nums1, k)
        if len(nums1) == 0:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])
        m = len(nums1)
        n = len(nums2)
        pa = min( k / 2, m)
        pb = k - pa
        if nums1[pa-1] > nums2[pb-1]:
            return self.findKth(nums1, nums2[pb:], k - pb)
        else:
            return self.findKth(nums1[pa:], nums2, k - pa)

if __name__ == '__main__':
    solution = Solution()
    print solution.findMedianSortedArrays([1,2], [1])


