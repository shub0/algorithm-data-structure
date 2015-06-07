#! /usr/bin/python

'''
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.
'''

class Solution:
    def align(self, words, maxWidth):
        num_words = len(words)
        if num_words == 1:
            return words[0] + ' ' * (maxWidth - len(words[0]))
        size = sum(map(len, words))
        if num_words == 2:
            return words[0] + ' ' * (maxWidth - size) + words[1]
        space = ' ' * ((maxWidth - size) / (num_words - 1))
        line  = space.join(words[1:])
        return words[0] + ' ' * (maxWidth - len(line) - len(words[0])) + line

    # @param {string[]} words
    # @param {integer} maxWidth
    # @return {string[]}
    def fullJustify(self, words, maxWidth):
        size_array = map(len, words)
        num_words  = len(size_array)
        curr_len   = 0
        start_index = 0
        text = list()
        for index in range(num_words):
            curr_len += size_array[index] # put the word in the current line
            curr_len += 1 # space
            if index+1 < num_words and curr_len + size_array[index+1] <= maxWidth:
                continue
            text.append(self.align(words[start_index: index+1], maxWidth))
            start_index = index + 1
            curr_len = 0
        return text

if __name__ == '__main__':
    solution = Solution()
    print solution.fullJustify(	["What","must","be","shall","be."], 12)
