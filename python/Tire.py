'''
Implement a trie with insert, search, and startsWith methods.
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

class Trie(object):

    def __init__(self):
        self.root = TrieNode(".")

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cursor = self.root
        for char in word:
            if char not in cursor.children:
                cursor.children[char] = TrieNode(char)
            cursor = cursor.children[char]
        cursor.size += 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cursor = self.root
        for char in word:
            if char not in cursor.children:
                return False
            cursor = cursor.children[char]
        return cursor.size > 0

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cursor = self.root
        for char in prefix:
            if char not in cursor.children:
                return False
            cursor = cursor.children[char]
        return True

# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("somestring")
print trie.search("key")
trie.insert("key")
print trie.search("key")
print trie.startsWith("some")
print trie.search("some")
