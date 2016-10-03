'''
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
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

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode(".")

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cursor = self.root
        for char in word:
            if char not in cursor.children:
                cursor.children[char] = TrieNode(char)
            cursor = cursor.children[char]
        cursor.size += 1

    def searchRecursive(self, node, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type node: TrieNode
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return node.size > 0
        char = word[0]
        if char == '.':
            for child in node.children.values():
                if self.searchRecursive(child, word[1:]):
                    return True
            return False
        if char in node.children:
            child = node.children[char]
            return self.searchRecursive(child, word[1:])
        return False

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.searchRecursive(self.root, word)

wordDictionary = WordDictionary()
wordDictionary.addWord("word")
print wordDictionary.search("word")
print wordDictionary.search("pattern")
print wordDictionary.search("wo.d")
print wordDictionary.search("wor")
