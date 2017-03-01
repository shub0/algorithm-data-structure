"""
Think about Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G), and white(W). You also have several balls in your hand.

Each time, you may choose a ball in your hand, and insert it into the row (including the leftmost place and rightmost place). Then, if there is a group of 3 or more balls in the same color touching, remove these balls. Keep doing this until no more balls can be removed.

Find the minimal balls you have to insert to remove all the balls on the table. If you cannot remove all the balls, output -1.

Examples:

Input: "WRRBBW", "RB"
Output: -1
Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW

Input: "WWRRBBWW", "WRBRW"
Output: 2
Explanation: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty

Input:"G", "GGGGG"
Output: 2
Explanation: G -> G[G] -> GG[G] -> empty

Input: "RBYYBBRRB", "YRBGB"
Output: 3
Explanation: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty

Note:
You may assume that the initial row of balls on the table won't have any 3 or more consecutive balls with the same color.
The number of balls on the table won't exceed 20, and the string represents these balls is called "board" in the input.
The number of balls in your hand won't exceed 5, and the string represents these balls is called "hand" in the input.
Both input strings will be non-empty and only contain characters 'R','Y','B','G','W'.
"""
import collections
class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        self.maxCount = len(hand) + 1
        hands = collections.Counter(hand)
        res = self.helper(board + "#", hands)
        return -1 if res == self.maxCount else res

    def helper(self, board, hands):
        board = self.clean(board)
        if board == "#":
            return 0
        start = 0
        res = self.maxCount
        for end in range(len(board)):
            if board[start] == board[end]:
                continue
            needed = 3 - (end - start)
            if hands[ board[start] ] >= needed:
                hands[ board[start] ] -= needed
                res = min(res, needed + self.helper(board[:start] + board[end:], hands))
                hands[ board[start] ] += needed
            start = end
        return res

    def clean(self, board):
        start = 0
        for end in range(len(board)):
            if board[start] == board[end]:
                continue
            if end - start >= 3:
                return self.clean(board[:start] + board[end:])
            start = end
        return board

solution = Solution()
print solution.findMinStep("WRRBBW", "RB")
print solution.findMinStep("WWRRBBWW", "WRBRW")
print solution.findMinStep("RBYYBBRRB", "YRBGB")
