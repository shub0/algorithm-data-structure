'''
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.

'''

class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        output = [0] * n
        curr = 1
        for index in range(n):
            output[index] = curr
            # DFS
            if curr * 10 <= n:
                curr *= 10
            # back-tracking
            else:
                if curr >= n:
                    curr /= 10
                curr += 1
                while (curr % 10 == 0):
                    curr /= 10
        return output

    def lexicalOrderDFS(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        output = list()

        def dfs(num):
            if num > n:
                return
            output.append(num)
            for i in range(10):
                dfs(10*num+i)

        for index in range(1,10):
            dfs(index)
        return output

solution = Solution()
print solution.lexicalOrder(10)
print solution.lexicalOrderDFS(13)
