'''
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
'''


class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        output = list()
        if not matrix:
            return output
        self.directions = [ (0,1), (0,-1), (1,0), (-1,0) ]
        row = len(matrix)
        col = len(matrix[0])
        p_visited = [ [False] * col for _ in range(row) ]
        a_visited = [ [False] * col for _ in range(row) ]
        for r in range(row):
            self.dfs(matrix, r, 0, p_visited, row, col)
            self.dfs(matrix, r, col-1, a_visited, row, col)
        for c in range(col):
            self.dfs(matrix, 0, c, p_visited, row, col)
            self.dfs(matrix, row-1, c, a_visited, row, col)
        for r in range(row):
            for c in range(col):
                if p_visited[r][c] and a_visited[r][c]:
                    output.append( (r, c) )
        return output

    def dfs(self, matrix,  r, c, visited, row, col):
        visited[r][c] = True
        for dir in self.directions:
            next_r, next_c = r + dir[0], c + dir[1]
            if next_r < 0 or next_r >= row or \
               next_c < 0 or next_c >= col or \
               visited[next_r][next_c] or matrix[next_r][next_c] < matrix[r][c]:
                continue
            self.dfs(matrix, next_r, next_c, visited, row, col)

solution = Solution()
matrix = [[1,2,2,3,5], [3,2,3,4,4], [2,4,5,3,1], [6,7,1,4,5], [5,1,1,2,4]]
matrix = [[1,1], [1,1], [1,1]]
print solution.pacificAtlantic(matrix)
