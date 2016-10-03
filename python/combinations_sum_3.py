'''
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
'''

class Solution(object):
    def combinationSum3(self, size, target):
        """
        :type size: int
        :type target: int
        :rtype: List[List[int]]
        """
        max_num  = target
        self.output = list()
        self.makeCombination(1, 9, target, size, list())
        return self.output

    def makeCombination(self, start, end, target, left_size, a_comb):
        if (target == 0 and 0 == left_size):
            self.output.append(a_comb[:])
        if (left_size * start <= target):
            for index in range(start, end+1):
                a_comb.append(index)
                self.makeCombination(index+1, end, target-index, left_size-1, a_comb)
                a_comb.pop()

solution = Solution()
print solution.combinationSum3(3, 7)
