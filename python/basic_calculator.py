#! /usr/bin/python

'''
Write a programm to evaluate the result of a mathmatical expressions and count for the priority of operaters
supported operators are +, -, *, /, ^ and parenthesis
Input is space separated string

for example:
15 + 4 * 3 = 27
(15 + 4) * 3 = 57
'''

import operator
class Calculator:
    def __init__(self, input_string, vars={}):
        self.tokens = list(input_string)
        self.num_tokens = len(self.tokens)
        self.index = -1
        self.const = {
            'pi': 3.1415926835,
            'e' : 2.718281828459045
        }
        self.operator = set('+-*/()^')
        for var in vars.keys():
            if self.const.get(var) != None:
                raise Exception('Cannot redefine values of ' + var)
            self.const[var] = vars[var]
        self.TERMINATOR = '#'

    def peek(self):
        while self.index < self.num_tokens - 1:
            # Skip white space
            if self.tokens[self.index+1] != ' ':
                break
            self.index += 1
        if self.index < self.num_tokens - 1:
            return self.tokens[self.index+1]
        return self.TERMINATOR

    def value(self):
        token = list()
        while self.peek() not in self.operator and self.peek() != self.TERMINATOR:
            token.append(self.peek())
            self.index += 1
        str_token = ''.join(token).strip()
        if str_token.isdigit():
            return float(str_token)
        return self.const.get(str_token,1)

    def negative(self):
        token = self.peek()
        if token == '-':
            self.index += 1
            return -1 * self.parenthesis()
        else:
            return self.value()

    def parenthesis(self):
        token = self.peek()
        if token == '(':
            self.index += 1
            value = self.addition()
            if self.peek() != ')':
                raise Exception('No matched parenthesis')
            self.index += 1
            return value
        else:
            return self.negative()

    def multiplication(self):
        values = [self.power()]
        while True:
            token = self.peek()
            if token == '*':
                self.index += 1
                values.append(self.parenthesis())
            elif token == '/':
                self.index += 1
                denominator = self.parenthesis()
                if denominator == 0:
                    raise ValueError('Denominator = 0')
                values.append (1.0 / denominator)
            else:
                break
        return reduce(operator.mul, values)

    def power(self):
        values = [ self.parenthesis() ]
        while True:
            token = self.peek()
            if token == '^':
                self.index += 1
                values.append(self.parenthesis())
            else:
                break
        result = values[0]
        for val in values[1:]:
            result = result ** val
        return result

    def addition(self):
        values = [ self.multiplication() ]
        while True:
            token = self.peek()
            if token == '+':
                self.index += 1
                values.append(self.multiplication())
            elif token == '-':
                self.index += 1
                values.append(-1*self.multiplication())
            else:
                break
        return reduce(operator.add, values)

class Solution:
    def calculate(self, input_string):
        parser = Calculator(input_string)
        return int(parser.addition())

if __name__ == '__main__':
    solution = Solution()
    print solution.calculate("(1+(4+5+2)-3)+(6+8)")
