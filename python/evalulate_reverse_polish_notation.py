#! /usr/bin/python

'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = list()
        import operator
        supported_operators ={'+': operator.add,
                              '-': operator.sub,
                              '*': operator.mul,
                              '/': operator.truediv}
        for token in tokens:
            if token in supported_operators.keys():
                num_1 = stack.pop()
                num_2 = stack.pop()
                stack.append(int(supported_operators[token](num_2, num_1)))
            elif token.isdigit():
                stack.append(int(token))
        return stack[0]

if __name__ == '__main__':
    solution = Solution()
    print solution.evalRPN(["2", "-1", "+", "3", "*"])
    print solution.evalRPN(["4", "13", "5", "/", "+"])
    print solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
