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
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        size = len(words)
        current_len = 0
        current = list()
        output = list()
        index = 0
        while index < size:
            current_len += len(words[index])
            if current_len <= maxWidth:
                current.append(words[index])
                current_len += 1
                index += 1
            else:
                output.append(self.makeLine(current, maxWidth))
                current_len = 0
                current = list()
        output.append(self.makeLineLast(current, maxWidth))
        return output

    def makeLineLast(self, words, maxWidth):
        size = len(words)
        if size == 0:
            return " " * maxWidth
        line = " ".join(words)
        return line + " " * (maxWidth - len(line))

    def makeLine(self, words, maxWidth):
        size = len(words)
        if size == 0:
            return " " * maxWidth
        word_size = sum(map(lambda x: len(x), words))
        if size == 1:
            return words[0] + " " * ( maxWidth - word_size )
        std_space = (maxWidth - word_size) / (size - 1)
        space = " " * std_space
        extra_space = maxWidth - std_space * (size-1) - word_size
        big_space = " " * (std_space + 1)
        return big_space.join(words[:extra_space + 1]) + space + space.join(words[extra_space+1:])

if __name__ == '__main__':
    solution = Solution()
    output =  solution.fullJustify2(["Don't","go","around","saying","the","world","owes","you","a","living;","the","world","owes","you","nothing;","it","was","here","first."], 30)
    print output
    print map(lambda x: len(x), output)
