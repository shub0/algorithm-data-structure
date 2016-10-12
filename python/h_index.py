'''
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N - h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

Note: If there are several possible values for h, the maximum one is taken as the h-index
'''

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        size = len(citations)
        counts = [0] * (size+1)
        for citation in citations:
            if citation >= size:
                counts[size] += 1
            else:
                counts[citation] += 1
        acc = 0
        for index in range(size, -1, -1):
            acc += counts[index]
            if acc >= index:
                return index
        return 0

    def hIndex2(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        low = 0
        high = len(citations)
        while (low < high):
            mid = (high - low) / 2 + low
            right = size - mid + 1
            if right > citations[mid]:
                low = mid + 1
            elif right < citation:
                high = mid
            else:
                return right
        return size - low

solution = Solution()
print solution.hIndex([1,4,5,6,8,9,10])
