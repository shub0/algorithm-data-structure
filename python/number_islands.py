#! /usr/bin/python

'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
'''

class Solution:
    def adjacentPixel(self, pixel, grid):
        adjacent_pixel = set()
        pixel_row, pixel_col = pixel
        if pixel_row+1 < len(grid) and grid[pixel_row+1][pixel_col] == '1':
            adjacent_pixel.add( (pixel_row+1, pixel_col) )
        if pixel_col+1 < len(grid[0]) and grid[pixel_row][pixel_col+1] == '1':
            adjacent_pixel.add( (pixel_row, pixel_col+1) )
        if pixel_row-1 >=0  and grid[pixel_row-1][pixel_col] == '1':
            adjacent_pixel.add( (pixel_row-1, pixel_col) )
        if pixel_col-1 >= 0  and grid[pixel_row][pixel_col-1] == '1':
            adjacent_pixel.add( (pixel_row, pixel_col-1) )
        return adjacent_pixel

    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        if not grid:
            return 0
        row       = len(grid)
        col       = len(grid[0])
        count     = 0
        open_set  = set()
        close_set = set()
        for index_row in range(row):
            for index_col in range(col):
                if grid[index_row][index_col] == '0' or (index_row, index_col) in close_set:
                    continue
                open_set.add( (index_row, index_col) )
                count += 1
                # BFS
                while len(open_set) > 0:
                    pixel = open_set.pop()
                    (pixel_row, pixel_col) = pixel
                    close_set.add( (pixel_row, pixel_col) )
                    adjacent_pixel = self.adjacentPixel(pixel, grid)
                    open_set.update( adjacent_pixel - close_set )
        return count


if __name__ == '__main__':
    solution = Solution()
    grid1 = ['11110', '11010', '11000', '00000']
    grid2 = ['11000', '11000', '00100', '00011']
    grid3 = ["111","010","111"]
    print solution.numIslands(grid1)
    print solution.numIslands(grid2)
    print solution.numIslands(grid3)
