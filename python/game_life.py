'''
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.
'''

class Solution(object):
    def nnb(self, board, row, col):
        count = sum([board[i][j]%2 for i in range(row-1,row+2) for j in range(col-1,col+2) if 0 <= i < self.ROW and 0<= j < self.COL]) - (board[row][col])
        return count

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # 0 dead, 1 live
        # 2 dead -> live, 3 live -> dead
        self.ROW = len(board)
        if self.ROW < 1:
            return
        self.COL = len(board[0])

        for row in range(self.ROW):
            for col in range(self.COL):
                count = self.nnb(board, row, col)
                if (board[row][col] == 1):
                    # under-population / over-population
                    if count < 2 or count > 3:
                        board[row][col] = 3
                else:
                    # reproduction
                    if count == 3:
                        board[row][col] = 2

        # Set numbers
        for row in range(self.ROW):
            for col in range(self.COL):
                if board[row][col] == 2:
                    board[row][col] = 1
                if board[row][col] == 3:
                    board[row][col] = 0

solution = Solution()
matrix = [[0,0,1], [1,0,1], [0,0,1]]
solution.gameOfLife(matrix)
print matrix
