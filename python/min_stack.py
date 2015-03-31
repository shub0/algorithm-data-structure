#! /usr/bin/python
'''

 Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

'''
class MinStack:
    def __init__(self):
        self.data = list()
        self.min  = list()

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.data.append(x)
        if len(self.min) == 0 or x <= self.min[-1]:
            self.min.append(x)

    # @return nothing
    def pop(self):
        top = self.data.pop()
        if top == self.min[-1]:
            self.min.pop()

    # @return an integer
    def top(self):
        return self.data[-1]

    # @return an integer
    def getMin(self):
        return self.min[-1]

if __name__ == '__main__':
    min_stack = MinStack()
    min_stack.push(1)
    min_stack.push(-3)
    min_stack.push(-3)
    print min_stack.getMin()
    min_stack.push(3)
    print min_stack.getMin()
    print min_stack.top()
    min_stack.pop()
    print min_stack.getMin()
    min_stack.pop()
    print min_stack.getMin()
    min_stack.pop()
    print min_stack.getMin()
