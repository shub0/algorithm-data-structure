#! /usr/bin/python

'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.
'''

class Solution:
    def countAndSay(self, n):
        sequence = ['1']
        for index in range(1, n):
            sequence.append(self.generate(sequence[index-1]))
        return sequence[n-1]

    # @param {string} orig_string
    # @return {string}
    def generate(self, orig_string):
        count_string = list()
        count = 0
        for index in range(len(orig_string)):
            char = orig_string[index]
            if index > 0 and orig_string[index] != orig_string[index-1]:
                count_string.append('%s' % count)
                count_string.append(orig_string[index-1])
                count = 1
            else:
                count += 1
        count_string.append('%s' % count)
        count_string.append(orig_string[-1])

        return ''.join(count_string)

if __name__ == '__main__':
    solution = Solution()
    print solution.countAndSay(5)
