'''
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"]
'''

class TrieNode(object):
    def __init__(self, char):
        """
        Initialize your data structure here.
        """
        import collections
        self.char = char
        self.size = 0
        self.children = dict()

class Solution(object):
    def findNeighbours(self, pixel):
        row = pixel[0]
        col = pixel[1]
        neighbours = set()
        if row - 1 > -1:
            neighbours.add( (row-1, col) )
        if row + 1 < self.ROW:
            neighbours.add( (row+1, col) )
        if col - 1 > -1:
            neighbours.add( (row, col-1) )
        if col + 1< self.COL:
            neighbours.add( (row, col+1) )
        return neighbours

    def buildOnePath(self, node, pixel):
        neighbours = self.findNeighbours(pixel)
        for neighbour in neighbours:
            if self.board[neighbour[0]][neighbour[1]] == "*":
                continue
            char = self.board[neighbour[0]][neighbour[1]]
            self.board[neighbour[0]][neighbour[1]] = "*"
            if char not in node.children:
                node.children[char] = TrieNode(char)
            next = node.children[char]
            self.buildOnePath(next, neighbour)
            self.board[neighbour[0]][neighbour[1]] = char

    def buildTrie1(self, board):
        self.root = TrieNode(".")
        self.board = board
        self.ROW = len(board)
        self.COL = len(board[0])
        for row in range(self.ROW):
            for col in range(self.COL):
                visited = set()
                pixel = (row, col)
                visited.add(pixel)
                char = self.board[row][col]
                self.board[row][col] = "*"
                if char not in self.root.children:
                    self.root.children[char] = TrieNode(char)
                next = self.root.children[char]
                self.buildOnePath(next, pixel)
                self.board[row][col] = char

    def search(self, word):
        cursor = self.root
        for char in word:
            if char not in cursor.children:
                return False
            cursor = cursor.children[char]
        return True

    def findWords1(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.buildTrie1(board)
        return list(set(filter(lambda x: self.search(x), words)))


    def buildTrie2(self, words):
        root = TrieNode(".")
        for word in words:
            cursor = root
            for char in word:
                if char not in cursor.children:
                    cursor.children[char] = TrieNode(char)
                cursor = cursor.children[char]
            cursor.size += 1
        return root

    def findNeighbours(self, pos):
        row = pos[0]
        col = pos[1]
        neighbours = set()
        if row > 0:
            neighbours.add( (row-1, col) )
        if row+1 < self.ROW:
            neighbours.add( (row+1, col) )
        if col > 0:
            neighbours.add( (row, col-1) )
        if col+1 < self.COL:
            neighbours.add( (row, col+1) )
        return neighbours

    def dfs(self, node, word, pos, visited):
        row = pos[0]
        col = pos[1]
        char = self.board[row][col]
        if char not in node.children:
            return
        visited.add(pos)
        word.append( char )
        next = node.children[char]
        if next.size > 0:
            self.output.add( "".join(word) )
        neighbours = self.findNeighbours(pos) - visited
        for neighbour in neighbours:
            size = len(word)
            self.dfs(next, word, neighbour, visited)
            word = word[:size]
        word = word[:-1]
        visited.remove(pos)

    def findWords2(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = self.buildTrie2(words)
        self.output = set()
        self.ROW = len(board)
        if (self.ROW < 1):
            return []
        self.COL = len(board[0])
        self.board = board
        for row in range(self.ROW):
            for col in range(self.COL):
                self.dfs(root, list(), (row, col), set())
        return list(self.output)

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        row = len(board)
        col = len(board[0])
        size = len(words)
        if size > (1000 * row * col):
            return self.findWords1(board, words)
        else:
            return self.findWords2(board, words)

    def findWords3(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        def DFS(path, i, j, root):
            if '#' in root:
                output.add(path)
            if i < 0 or j < 0 or i > m - 1 or j > n - 1 or board[i][j] not in root:
                return
            char = board[i][j]
            board[i][j] = "*"
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                DFS(path + char, x,  y, root[char])
            board[i][j] = char

        if not board: return []
        root = dict()
        for word in words:
            cursor = root
            for char in word:
                if char not in cursor:
                    cursor[char] = {}
                cursor = cursor[char]
            cursor['#'] = '#'
        output = set()
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                DFS("", i, j, root)
        return list(output)
