#! /usr/bin/python

'''
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
'''

class Solution:
    def is_palindrome(self, s):
        return s ==  s[::-1]

    # @param {string} s
    # @return {string}
    def longestPalindrome2(self, s):
        size = len(s)
        if size == 0:
            return ''
        start = 0
        end = 1
        for index in range(size):
            current_start = index
            current_end = size
            while current_end > current_start:
                if self.is_palindrome(s[current_start:current_end]):
                    break
                if current_end - current_start < end - start:
                    break
                current_end -= 1
            if current_end - current_start > end - start:
                start = current_start
                end = current_end
        return s[start:end]

    def longestPalindrome(self, s):
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range(1, n - 1):
            P[i] = (R > i) and min(R-i, P[2*C-i])
            while T[i+1 + P[i]] == T[i-1 - P[i]]:
                P[i] += 1
                if i + P[i] > R:
                    C, R = i, i + P[i]
        max_len, center_index = max((n, i) for i, n in enumerate(P))
        return s[(center_index - max_len)//2 : (center_index + max_len)//2]

if __name__ == '__main__':
    solution = Solution()
    print solution.longestPalindrome('rgczcpratwyqxaszbuwwcadruayhasynuxnakpmsyhxzlnxmdtsqqlmwnbxvmgvllafrpmlfuqpbhjddmhmbcgmlyeypkfpreddyencsdmgxysctpubvgeedhurvizgqxclhpfrvxggrowaynrtuwvvvwnqlowdihtrdzjffrgoeqivnprdnpvfjuhycpfydjcpfcnkpyujljiesmuxhtizzvwhvpqylvcirwqsmpptyhcqybstsfgjadicwzycswwmpluvzqdvnhkcofptqrzgjqtbvbdxylrylinspncrkxclykccbwridpqckstxdjawvziucrswpsfmisqiozworibeycuarcidbljslwbalcemgymnsxfziattdylrulwrybzztoxhevsdnvvljfzzrgcmagshucoalfiuapgzpqgjjgqsmcvtdsvehewrvtkeqwgmatqdpwlayjcxcavjmgpdyklrjcqvxjqbjucfubgmgpkfdxznkhcejscymuildfnuxwmuklntnyycdcscioimenaeohgpbcpogyifcsatfxeslstkjclauqmywacizyapxlgtcchlxkvygzeucwalhvhbwkvbceqajstxzzppcxoanhyfkgwaelsfdeeviqogjpresnoacegfeejyychabkhszcokdxpaqrprwfdahjqkfptwpeykgumyemgkccynxuvbdpjlrbgqtcqulxodurugofuwzudnhgxdrbbxtrvdnlodyhsifvyspejenpdckevzqrexplpcqtwtxlimfrsjumiygqeemhihcxyngsemcolrnlyhqlbqbcestadoxtrdvcgucntjnfavylip')
