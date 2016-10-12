'''
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Examples:
"123", 6 -> ["1+2+3", "1*2*3"]
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
'''

class Solution(object):
    def findExpression(self, expr, num, prev_val, curr_val):
        if (len(num) == 0) and (curr_val == self.target):
            self.output.add(expr[:])
        elif (len(num) > 0):
            max_len = len(num)
            if num[0] == '0':
                max_len = 1
            for index in range(max_len):
                val = num[:index+1]
                num_val = int(val)
                self.findExpression(expr+"+"+val, num[index+1:],  num_val, curr_val+num_val)
                self.findExpression(expr+"-"+val, num[index+1:], -num_val, curr_val-num_val)
                self.findExpression(expr+"*"+val, num[index+1:], prev_val*num_val, (curr_val-prev_val) + prev_val*num_val)

    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.output = set()
        self.target = target
        size = len(num)
        if num[0] == "0":
            size = 1
        for index in range(size):
            self.findExpression(num[:index+1], num[index+1:], int(num[:index+1]), int(num[:index+1]))

        return list(self.output)


solution = Solution()
print solution.addOperators("123", 6)
print solution.addOperators("232", 8)
print solution.addOperators("105", 5)
print solution.addOperators("3456237490", 9191)
