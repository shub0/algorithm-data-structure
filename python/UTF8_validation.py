'''
A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

For 1-byte character, the first bit is a 0, followed by its unicode code.
For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.
This is how the UTF-8 encoding would work:

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Given an array of integers representing the data, return whether it is a valid utf-8 encoding.

data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.

Return true.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
Example 2:

data = [235, 140, 4], which represented the octet sequence: 11101011 10001100 00000100.

Return false.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.
'''

class Solution(object):
    def validUtf8(self, nums):
        def check(nums, begin, size):
            for i in range(begin + 1, begin + size + 1):
                if i >= len(nums) or (nums[i] >> 6) != 0b10:
                    return False
            return True

        start = 0
        while start < len(nums):
            first = nums[start]
            if (first >> 3) == 0b11110 and check(nums, start, 3):
                start += 4
            elif (first >> 4) == 0b1110 and check(nums, start, 2):
                start += 3
            elif (first >> 5) == 0b110 and check(nums, start, 1):
                start += 2
            elif (first >> 7) == 0:
                start += 1
            else:
                return False
        return True
