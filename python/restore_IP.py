#! /usr/bin/python

'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
'''

class Solution:
    def validSegment(self, s):
        if len(s) == 0:
            return False
        if len(s) > 1 and s[0] == '0':
            return False
        num = int(s)
        return num >= 0 and num < 256

    def validIpAddress(self, s):
        return all(self.validSegment(segment) for segment in s.split('.'))

    def restoreIpRecursive(self, s, depth, ip_address, output):
        if depth == 3:
            output.append(ip_address[1:]+'.'+s)
        else:
            for index in range(1,len(s)):
                segment = s[:index]
                if not self.validSegment(segment):
                    break
                self.restoreIpRecursive(s[index:], depth + 1, ip_address+'.'+segment, output)

    def restoreIpAddresses(self, s):
        output = list()
        self.restoreIpRecursive(s, 0, '', output)
        return filter(lambda x: self.validIpAddress(x), output)

    # @param s, a string
    # @return a list of strings
    def restoreIpAddressesLong(self, s):
        size = len(s)
        if size < 4 or size > 12:
            return []
        output = list()
        for index1 in range(size):
            for index2 in range(index1+1, size):
                for index3 in range(index2+1, size):
                        segment1 = s[0:index1]
                        segment2 = s[index1:index2]
                        segment3 = s[index2:index3]
                        segment4 = s[index3:]
                        if self.validSegment(segment1) and self.validSegment(segment2) and self.validSegment(segment3) and self.validSegment(segment4):
                            output.append('%s.%s.%s.%s' % (segment1, segment2, segment3, segment4))
        return output


if __name__ == '__main__':
    solution = Solution()
    print solution.validIpAddress('255.1.1.0')
    print solution.restoreIpAddresses('010010')
