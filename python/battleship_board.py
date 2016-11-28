'''
Given an 2D board, count how many different battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:

You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
Example:
X..X
...X
...X
In the above board there are 2 battleships.
Invalid Example:
...X
XXXX
...X
This is an invalid board that you will not receive - as battleships will always have a cell separating between them.

Follow up:
Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?

'''
class Solution(object):

    def dfs(self, r, c, row, col, board, visited):
        for direction in self.directions:
            next_r, next_c = r + direction[0], c + direction[1]
            if (next_r >= 0) and (next_r < row) and (next_c >= 0 and next_c < col) and \
               ((next_r, next_c) not in visited) and (board[next_r][next_c] == 'X'):
                visited.add( (next_r, next_c) )
                self.dfs(next_r, next_c, row, col, board, visited)

    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board:
            return 0
        self.directions = ( (1, 0), (-1, 0), (0, 1), (0, -1) )
        visited = set()
        row = len(board)
        col = len(board[0])
        count = 0
        for r in range(row):
            for c in range(col):
                if ( ((r, c) not in visited) and (board[r][c] == 'X') ):
                    count += 1
                    visited.add( (r, c) )
                    self.dfs(r, c, row, col, board, visited)
        return count

    def countBattleships2(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        if not board:
            return count
        row = len(board)
        col = len(board[0])
        for r in range(row):
            for c in range(col):
                if board[r][c] != "X":
                    continue
                if r > 0 and board[r-1][c] == "X":
                    continue
                if c > 0 and board[r][c-1] == "X":
                    continue
                count += 1
        return count

solution = Solution()
print solution.countBattleships(["X..X", "XXXX", "...X"])
print solution.countBattleships2(["X..X","...X", "...X"])
