'''
Letter Combinations of a Phone Number Total Accepted: 32660 Total Submissions: 123824 My Submissions Question Solution 
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''

class Solution:
    def __init__(self):
        self.keyboard = [ '0',   '1',    'abc', 'def', 'ghi', 
                          'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        self.combine_list = list()

    # @return a list of strings, [s1, s2]
    # Recursive is a DFS
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        self.makeLetterCombinations(digits, '')
        return self.combine_list

    # @param digits a string
    # @param word a string
    def makeLetterCombinations(self, digits, word):
        size = len(digits)
        if size == 0:
            self.combine_list.append(word)
            return
        digit = int(digits[0])
        for char in self.keyboard[digit]:
            word += char
            self.makeLetterCombinations(digits[1:], word)
            word = word[:-1]

    # @return a list of strings, [s1, s2]
    # Non-recursive is a BFS
    def letterCombinationsNonRecursive(self, digits):
        size = len(digits)
        if size == 0:
            return []
        digit = int(digits[0])
        combine_list = [ char for char in self.keyboard[digit] ]
        for index in range(1, size):
            digit = int(digits[index])
            chars = self.keyboard[digit]
            previous_list = combine_list
            combine_list = list()
            for char in chars:
                combine_list.extend([ word+char for word in previous_list ])
        return combine_list
    
if __name__ == '__main__':
    solution = Solution()
    print solution.letterCombinationsNonRecursive('23')
