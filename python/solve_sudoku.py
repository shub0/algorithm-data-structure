#! /usr/bin/python

'''
Write a program to solve a Sudoku puzzle by filling the empty cells.
Empty cells are indicated by the character '.'.
You may assume that there will be only one unique solution.
'''

class Solution:
    def check(self, index_row, index_col, board):
        char = board[index_row][index_col]
        board[index_row][index_col] = '.'
        for row in range(9):
            if board[row][index_col] == char:
                return False
        for col in range(9):
            if board[index_row][col] == char:
                return False
        for row in range(3):
            for col in range(3):
                if board[3*(index_row/3)+row][3*(index_col/3)+col] == char:
                    return False
        board[index_row][index_col] = char
        return True

    def dfs(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    continue
                for char in '123456789':
                    board[row][col] = char
                    if self.check(row, col, board) and self.dfs(board):
                        return True
                    board[row][col] = '.'
                return False
        return True

    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        self.dfs(board)
        
if __name__ == '__main__':
    solution = Solution()
    matrix = [['5','3','.','.','7','.','.','.','.'],
              ['6','.','.','1','9','5','.','.','.'],
              ['.','9','8','.','.','.','.','6','.'],
              ['8','.','.','.','6','.','.','.','3'],
              ['4','.','.','8','.','3','.','.','1'],
              ['7','.','.','.','2','.','.','.','6'],
              ['.','6','.','.','.','.','2','8','.'],
              ['.','.','.','4','1','9','.','.','5'],
              ['.','.','.','.','8','.','.','7','9']]
    
    print 'solution for %s ' % matrix
    solution.solveSudoku(matrix)
    print matrix

