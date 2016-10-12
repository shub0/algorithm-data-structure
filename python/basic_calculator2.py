'''
1.Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
'''

import operator
class Calculator(object):
    def __init__(self, formula):
        self.tokens = list(formula)
        self.size = len(self.tokens)
        self.index = -1
        self.operator = set("+-*/^()")

    def peek(self):
        while self.index < self.size-1:
            if self.tokens[self.index+1] != ' ':
                break
            self.index += 1
        if self.index < self.size-1:
            return self.tokens[self.index+1]

    def value(self):
        value = []
        while self.peek() not in self.operator and self.index < self.size-1:
            value.append(self.peek())
            self.index += 1
        str_value = "".join(value)
        if str_value.isdigit():
            return int(str_value)
        raise Exception("Unknown symbol " + str_value)

    def addition(self):
        value = self.mul()
        while True:
            token = self.peek()
            if token == "+":
                self.index += 1
                value += self.mul()
            elif token == "-":
                self.index += 1
                value -= self.mul()
            else:
                break
        return value

    def mul(self):
        value = self.power()
        while True:
            token = self.peek()
            if token == "*":
                self.index += 1
                value *= self.power()
            elif token == "/":
                self.index += 1
                value /= self.power()
            else:
                break
        return value

    def power(self):
        value = self.parenthesis()
        while True:
            token = self.peek()
            if token == "^":
                self.index += 1
                values = value ** self.parenthesis()
            else:
                break
        return value

    def parenthesis(self):
        token = self.peek()
        if token == "(":
            self.index += 1
            value = self.addition()
            if self.peek() != ")":
                raise Exception("No matched parenthesis")
            self.index += 1
            return value
        else:
            return self.negative()

    def negative(self):
        token = self.peek()
        if token == "-":
            self.index += 1
            return -1 * self.parenthesis()
        else:
            return self.value()

    def calculate(self):
        return int(self.addition())

class Solution:
    def calculate(self, input_string):
        parser = Calculator(input_string)
        return int(parser.calculate())

if __name__ == '__main__':
    solution = Solution()
    print solution.calculate("14/3*2")
