#! /usr/bin/python

'''
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
'''

class Solution:
    def neighbours(self, board, pixel):
        neighbours = set()
        row = pixel[0]
        col = pixel[1]
        ROW = len(board)
        COL = len(board[0])
        if row - 1 > -1 and board[row-1][col] == 'O':
            neighbours.add((row-1, col))
        if row + 1 < ROW and board[row+1][col] == 'O':
            neighbours.add((row+1, col))
        if col - 1 > -1 and board[row][col-1] == 'O':
            neighbours.add((row, col-1))
        if col + 1 < COL and board[row][col+1] == 'O':
            neighbours.add((row, col+1))
        return neighbours

    def surround(self, board, pixel, close_set):
        ROW = len(board)
        COL = len(board[0])
        open_set = set()
        open_set.add(pixel)
        surround = True
        adjacent_pixel = set()
        def boundary(pixel):
            row = pixel[0]
            col = pixel[1]
            return row == 0 or row == ROW-1 or col == 0 or col == COL-1
        while len(open_set) > 0:
            pixel = open_set.pop()
            close_set.add(pixel)
            if boundary(pixel):
                surround = False
            adjacent_pixel.add(pixel)
            neighbours = self.neighbours(board, pixel)
            open_set.update( neighbours - close_set )

        # flip board
        if surround:
            for pixel in adjacent_pixel:
                board[pixel[0]][pixel[1]] = 'X'

    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solve(self, board):
        if not board:
            return
        ROW = len(board)
        COL = len(board[0])
        close_set = set()
        for index_row in range(ROW):
            for index_col in range(COL):
                if (index_row, index_col) in close_set or board[index_row][index_col] == 'X':
                    continue
                pixel = (index_row, index_col)
                self.surround(board, pixel, close_set)


if __name__ == '__main__':
    solution = Solution()
    board = ["XXXX","XOOX", "XXOX", "XOXX"]
    solution.solve(board)
    print board
