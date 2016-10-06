'''
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.
'''

class Solution(object):
    def getSize(self, A, B, C, D):
        return abs(A-C) * abs(B-D)

    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        size1 = self.getSize(A,B,C,D)
        size2 = self.getSize(E, F, G,H)
        X = [A,C,E,G]
        Y = [B,D,F,H]
        X.sort()
        Y.sort()
        overlap = self.getSize(X[1], Y[1], X[2], Y[2])
        if (E > C or F > D) or (G < A or H < B):
            overlap = 0
        return size1+size2-overlap
