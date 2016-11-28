'''
Given a non-empty array of numbers, a0, a1, a2, ... , an-1, where 0 <= ai <= 2^31.

Find the maximum result of ai XOR aj, where 0 <= i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
'''

class Trie(object):

    def __init__(self):
        self.root = dict()

    def add(self, bins):
        cursor = self.root
        for char in bins:
            cursor = cursor.setdefault(char, {})
        cursor["_end_"] = int(bins, 2)

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        trie = Trie()
        for num in nums:
            bins = "{0:032b}".format(num)
            trie.add(bins)
        maxXor = 0
        for num in nums:
            cur = trie.root
            curXor = 0
            for bit in "{0:032b}".format(num):
                curXor *= 2
                if (bit == "0"):
                    if ("1" in cur):
                        curXor += 1
                        cur = cur["1"]
                    else:
                        cur = cur["0"]
                elif (bit == "1"):
                    if ("0" in cur):
                        curXor += 1
                        cur = cur["0"]
                    else:
                        cur = cur["1"]
            maxXor = max(maxXor, curXor)
        return maxXor

solution = Solution()
print solution.findMaximumXOR([3, 10, 5, 25, 2, 8])
print solution.findMaximumXOR([32,18,33,42,29,20,26,36,15,46])
