#! /usr/bin/python

'''
Implement the following operations of a stack using queues.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
'''

class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.queue = list()

    # @param x, an integer
    # @return nothing
    def push(self, x):
        queue_bk = list()
        queue_bk.append(x)
        while len(self.queue) > 0:
            queue_bk.append(self.queue.pop(0))
        self.queue = queue_bk

    # @return nothing
    def pop(self):
        return self.queue.pop(0)

    # @return an integer
    def top(self):
        return self.queue[0]

    # @return an boolean
    def empty(self):
        return len(self.queue) == 0

if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    print stack.top()
    print stack.pop()
