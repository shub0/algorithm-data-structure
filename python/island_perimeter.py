"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
"""

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        perimeter = 0
        row = len(grid)
        col = len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        def countNeighbours(r, c):
            count = 0
            for direction in directions:
                next_r, next_c = r+direction[0], c+direction[1]
                if next_r < 0 or next_r >= row:
                    continue
                if next_c < 0 or next_c >= col:
                    continue
                count += grid[next_r][next_c]
            return count
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    perimeter += 4
                    perimeter -= countNeighbours(r, c)
        return perimeter

solution = Solution()
print solution.islandPerimeter([[0,1,0,0],
                                [1,1,1,0],
                                [0,1,0,0],
                                [1,1,0,0]])
