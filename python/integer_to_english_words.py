'''
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2^31 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Hint:

Did you see a pattern in dividing the number into chunk of words? For example, 123 and 123000.
Group the number by thousands (3 digits). You can write a helper function that takes a number less than 1000 and convert just that chunk to words.
There are many edge cases. What are some good test cases? Does your code work with input such as 0? Or 1000010? (middle chunk is zero and should not be printed out)
'''

class Solution(object):
    base = ["", "Thousand", "Million", "Billion"]
    digit = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    def readChunk(self, num):
        output = list()
        if num >= 100:
            output.append(Solution.digit[num / 100])
            output.append("Hundred")
        num = num % 100
        if num < 20:
            output.append(Solution.digit[num])
        else:
            output.append(Solution.tens[num / 10])
            output.append(Solution.digit[num % 10])
        return " ".join(output)

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        output = list()
        count = 0
        while num > 0:
            chunk = num % 1000
            if chunk > 0:
                output.append(self.readChunk(chunk).strip() + " " + Solution.base[count])
            num /= 1000
            count += 1
        return " ".join(output[::-1]).strip()

solution = Solution()
print solution.readChunk(21)
print solution.readChunk(11)
print solution.readChunk(8)
print solution.readChunk(111)
print solution.readChunk(191)
print solution.readChunk(90)
print solution.numberToWords(121)
print solution.numberToWords(1000)
print solution.numberToWords(1119)
print solution.numberToWords(1000900203)
