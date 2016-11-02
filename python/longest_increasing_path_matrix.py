'''
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
'''

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        dist = [ [0] * col for _ in range(row) ]
        direction = ( (1, 0), (-1, 0), (0,1), (0, -1) )
        def dfs(x, y):
            if dist[x][y] > 0:
                return dist[x][y]
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if nx >= 0 and ny >= 0 and nx < row and ny < col and matrix[x][y] < matrix[nx][ny]:
                    dist[x][y] = max(dist[x][y], dfs(nx, ny))
            dist[x][y] += 1
            return dist[x][y]
        return max([dfs(r, c) for r in range(row) for c in range(col)])

solution = Solution()
nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
print solution.longestIncreasingPath(nums)
