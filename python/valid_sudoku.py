#! /usr/bin/python

'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
A partially filled sudoku which is valid.
Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

Additional problem:
Solve the Sudoku
'''

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        row = len(board)
        col = len(board[0])
        if row != 9 or col != 9:
            return False
        # check row wise
        for index_row in range(9):
            row_ht = [False] * 9
            for index_col in range(9):
                if board[index_row][index_col] == '.':
                    continue
                num = ord(board[index_row][index_col]) - ord('0')
                if num == 0 or row_ht[num-1]:
                    return False
                else:
                    row_ht[num-1] = True

        # check column wise
        for index_col in range(9):
            col_ht = [False] * 9
            for index_row in range(9):
                if board[index_row][index_col] == '.':
                    continue
                num = ord(board[index_row][index_col]) - ord('0')
                if num == 0 or col_ht[num-1]:
                    return False
                else:
                    col_ht[num-1] = True

        # check each 3*3 cell
        for index_row in range(0,9,3):
            for index_col in range(0,9,3):
                # check for current cell
                cell_ht = [False] * 9
                for num_row in range(0,3):
                    for num_col in range(0,3):
                        curr_row = index_row + num_row
                        curr_col = index_col + num_col
                        if board[curr_row][curr_col] == '.':
                            continue
                        num = ord(board[curr_row][curr_col]) - ord('0')
                        if num == 0 or cell_ht[num-1]:
                            return False
                        else:
                            cell_ht[num-1] = True
        return True
            
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
    board = ["....5..1.",
             ".4.3.....",
             ".....3..1",
             "8......2.",
             "..2.7....",
             ".15......",
             ".....2...",
             ".2.9.....",
             "..4......"]
    print solution.isValidSudoku(matrix)
    print solution.isValidSudoku(board)






