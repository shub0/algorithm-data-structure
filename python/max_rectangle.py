#! /usr/bin/python

class Solution:

    def maxHistogram(self, histogram):
        size = len(histogram)
        if size == 0:
            return 0
        min_stack = list()
        max_area = histogram[0]
        for index in range(size):
            if len(min_stack) == 0 or min_stack[-1][0] <= histogram[index]:
                min_stack.append((histogram[index], index))
            else:
                while len(min_stack) > 0 and min_stack[-1][0] > histogram[index]:
                    pair = min_stack.pop()
                    temp_area = pair[0] * (index - pair[1])
                    max_area = max(max_area, temp_area)
                min_stack.append((histogram[index], pair[1]))

        while len(min_stack) > 0:
            pair = min_stack.pop()
            temp_area = pair[0] * (size - pair[1])
            max_area = max(max_area, temp_area)
        return max_area

    def maximalRectangle(self, maxtrix):
        ROW = len(maxtrix)
        if ROW == 0:
            return 0
        COL = len(maxtrix[0])
        if COL == 0:
            return 0
        up = [ [1] * COL for index in range(ROW) ]
        down = [ [1] * COL for index in range(ROW) ]
        for col in range(COL):
            max_number = 1
            for row in range(0, ROW):
                if maxtrix[row][col] == '0':
                    max_number = 0
                up[row][col] = max_number
                max_number += 1

        for col in range(COL):
            max_number = 1
            for row in range(ROW-1, -1, -1):
                if maxtrix[row][col] == '0':
                    max_number = 0
                down[row][col] = max_number
                max_number += 1
        print up
        print down
        max_area = 0
        for row in range(ROW):
            up_area = self.maxHistogram(up[row])
            down_area = self.maxHistogram(down[row])
            max_area = max(max_area, max(up_area, down_area))
        return max_area


if __name__ == '__main__':
    solution = Solution()
    matrix = [ "1111", "1101", "1110" ]
    print solution.maximalRectangle(matrix)
