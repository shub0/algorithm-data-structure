'''
Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.

Note: 1 <= k <= n <= 10^9.

Example:

Input:
n: 13   k: 2

Output:
10

Explanation:
The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
'''

'''
A solution explaination:
https://discuss.leetcode.com/topic/64539/java-7ms-denary-trie-tree-solution-with-detailed-explanation
'''

class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        result = 1;
        k -= 1
        while k > 0:
            count = 0
            interval = [result, result+1]
            while interval[0] <= n:
                count += (min(n+1, interval[1]) - interval[0])
                interval = [10*interval[0], 10*interval[1]]

            # complete tree, move to next branch
            if k >= count:
                result += 1
                k -= count
            # incomplete tree, search in subtree
            else:
                result *= 10
                k -= 1
        return result

solution = Solution()
print solution.findKthNumber(4289384,1922239)
print solution.findKthNumber(9885387,8786251)
print solution.findKthNumber(13,2)
print solution.findKthNumber(10,3)
