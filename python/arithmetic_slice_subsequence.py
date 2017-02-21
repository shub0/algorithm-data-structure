'''
A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A subsequence slice of that array is any sequence of integers (P0, P1, ..., Pk) such that 0 <= P0 < P1 < ... < Pk < N.

A subsequence slice (P0, P1, ..., Pk) of array A is called arithmetic if the sequence A[P0], A[P1], ..., A[Pk-1], A[Pk] is arithmetic. In particular, this means that k >= 2.

The function should return the number of arithmetic subsequence slices in the array A.

The input contains N integers. Every integer is in the range of -2^31 and 2^31-1 and 0 <= N <= 1000. The output is guaranteed to be less than 2^(31-1).


Example:

Input: [2, 4, 6, 8, 10]

Output: 7

Explanation:
All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
'''

'''
Solution:
dp record the number of subsequence (no matter length) ended at i with incremnt of diff

The following solution will not pass TLE, but it is more concise.
A improvment will be check diff in dp[j] before operation (but it is ugly)
'''


class Solution(object):
    def numberOfArithmeticSlices(self, A, k=3):
        """
        :type A: List[int]
        :rtype: int
        """
        import collections
        size = len(A)
        res = 0
        dp = [ collections.defaultdict(int) for _ in range(size) ]
        for i in xrange(size):
            for j in xrange(i):
                diff = A[i] - A[j]
                dp_t = dp[j][diff] + 1
                # filter out subsequence with length < k
                # dp_t = 1 => there are 3 elements in the subsequence
                res += max(dp_t-k+2, 0)
                dp[i][diff] += dp_t
        return res

solution = Solution()
print solution.numberOfArithmeticSlices([2,4,6,8,10],4)
