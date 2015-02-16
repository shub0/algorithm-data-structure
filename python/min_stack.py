#! /usr/bin/python

class MinStack:
    def __init__(self):
        self.data_list = list()
        
    # @param x, an integer
    # @return an integer
    def push(self, x):
        if len(self.data_list) == 0:
            self.data_list.append((x,x))
        else:
            current_min = self.data_list[len(self.data_list)-1][1]
            self.data_list.append((x, min(current_min, x)))

    # @return nothing
    def pop(self):
        self.data_list.pop()

    # @return an integer
    def top(self):
        if len(self.data_list) == 0: return 0
        return self.data_list[len(self.data_list)-1][0]

    # @return an integer
    def getMin(self):
        if len(self.data_list) == 0: return 0
        return self.data_list[len(self.data_list)-1][1]

if __name__ == '__main__':
    min_stack = MinStack()
    min_stack.push(-3)
    print min_stack.getMin()
    min_stack.push(3)
    print min_stack.getMin()
    print min_stack.top()
