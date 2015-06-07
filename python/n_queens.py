#! /usr/bin/python

'''
The n-queens puzzle is the problem of placing n queens on an n*n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''

class Solution:

    def valid(self, row, col):
        import math
        for index in range(self.num_queens):
            if self.board[index] == col or math.fabs(index - row) == math.fabs(self.board[index] - col):
                return False
        return True

    def print_solution(self):
        solution = list()
        for row_index in range(self.num_queens):
            curr_row = list()
            for col_index in range(self.num_queens):
                if self.board[row_index] != col_index:
                    curr_row.append('.')
                else:
                    curr_row.append('Q')
            solution.append(''.join(curr_row))
        return solution

    # @return a list of lists of string
    def solveNQueens(self, n):
        import sys
        INIT_VALUE = sys.maxint
        self.num_queens = n
        self.board = [INIT_VALUE] * n
        self.solution_list = list()
        row_index, col_index = 0, 0
        # search solution rowwise
        while row_index < self.num_queens:
            # search positions columnwise
            while col_index < self.num_queens:
                if self.valid(row_index, col_index):
                    self.board[row_index] = col_index
                    col_index = 0
                    break
                col_index += 1
            # No solution found for current row
            if self.board[row_index] == INIT_VALUE:
                # back-tracked to row 0, stop searching
                if row_index == 0:
                    break
                # back-tracking to previous row
                row_index -= 1
                col_index = self.board[row_index] + 1
                self.board[row_index] = INIT_VALUE
                continue
            # Solution found for the last row
            if row_index == self.num_queens - 1:
                # record the solution
                self.solution_list.append(self.print_solution())
                # search for next solution
                col_index = self.board[row_index] + 1
                self.board[row_index] = INIT_VALUE
                continue
            row_index += 1
        return self.solution_list

if __name__ == '__main__':
    solution = Solution()
    print solution.solveNQueens(4)
