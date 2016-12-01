'''
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 <= N <= 500. All integers are in the range of -2^28 to 2^28 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

'''

class Solution(object):
    def fourSumCountSlow(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        import bisect
        sum1 = [ a + b for a in A for b in B ]
        sum2 = [ c + d for c in C for d in D ]
        sum1.sort()
        sum2.sort()
        res = 0
        for val in sum1:
            index1 = bisect.bisect_left(sum2, -val)
            index2 = bisect.bisect_left(sum2, -val+1)
            if index1 < len(sum2) and sum2[index1] == -val:
                res += (index2-index1)
        return res

    def fourSumCount(self, A, B, C, D):
        import collections
        AB = collections.Counter(a+b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)

solution = Solution()
#print solution.fourSumCount([1,2], [-2,-1], [-1,2], [0,2])
print solution.fourSumCount([-1,-1],[-1,1],[-1,1],[1,-1])
