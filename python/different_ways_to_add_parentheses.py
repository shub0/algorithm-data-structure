'''
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.
'''
class Solution(object):
    import operator
    ops = {"+": operator.add,
           "-": operator.sub,
           "*": operator.mul
    }
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        size = len(input)
        if input.isdigit():
            return [int(input)]
        output = []
        for (index, char) in enumerate(input):
            if char not in Solution.ops:
                continue
            left = self.diffWaysToCompute(input[:index])
            right = self.diffWaysToCompute(input[index+1:])
            output.extend([Solution.ops[char](a,b) for a in left for b in right])
        return output

        '''
        return [a + b if ops == "+" else a-b if ops=="-" else a*b
                for i, ops in enumerate(input) if ops in "+-*"
                for a in self.diffWaysToCompute(input[:i])
                for b in self.diffWaysToCompute(input[i+1:])] or [int(input)]
        '''

solution = Solution()
print solution.diffWaysToCompute("2*3-4*5")
