#! /usr/bin/python

'''
 Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t

To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t

We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a

We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
'''

bclass Solution:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    def isScramble(self, s1, s2):
        solution_dict = dict()
        return self.scrambleStringDP(s1, s2, solution_dict)

    def scrambleStringDP(self, s1, s2, dp_dict):
        if (s1, s2) in dp_dict:
            return dp_dict[(s1, s2)]
        if len(s1) == 1:
            return s1 == s2
        elif sorted(s1) != sorted(s2):
            return False

        for index in range(len(s1)):
            if (self.scrambleStringDP(s1[:index], s2[-index:], dp_dict) and self.scrambleStringDP(s1[index:], s2[:-index], dp_dict)) \
               or (self.scrambleStringDP(s1[:index], s2[:index], dp_dict) and self.scrambleStringDP(s1[index:], s2[index:], dp_dict)):
                dp_dict[(s1,s2)] = True
                return True
        dp_dict[(s1, s2)] = False
        return False

if __name__ == '__main__':
    solution = Solution()
    print solution.isScramble('great', 'rgtae')
