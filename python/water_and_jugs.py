'''
You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True
Example 2:

Input: x = 2, y = 6, z = 5
Output: False
'''

class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        def isOdd(a):
            return (a&1) > 0

        def gcd(a, b):
            if (a == b):
                return b
            elif (a < b):
                return gcd(b, a)
            elif (isOdd(a) and not isOdd(b)):
                return gcd(a, b >> 1)
            elif (not isOdd(a) and isOdd(b)):
                return gcd(a >> 1, b)
            elif (not isOdd(a) and not isOdd(b)):
                return (gcd(a >> 1, b >> 1) << 1)
            return gcd(a-b, b)
        if (x < y):
            return self.canMeasureWater(y, x, z)
        if y == 0 and x == z or z == 0:
            return True
        elif y == 0 and x != z or x+y<z:
            return False
        denom = gcd(x, y)
        return z % denom == 0

solution = Solution()
print solution.canMeasureWater(3, 5, 4)
print solution.canMeasureWater(2, 6, 5)
print solution.canMeasureWater(104579, 104593, 12444)
