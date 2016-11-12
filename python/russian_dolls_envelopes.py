'''
You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Example:
Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
'''


class Solution(object):
    def binarySearch(self, array, width, height):
        left = 0
        right = len(array) - 1
        while left < right:
            mid = (right - left) / 2 + left
            if array[mid][1] > height:
                right = mid
            else:
                left = mid+1
        return right

    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # Sort by width
        envelopes = sorted(envelopes,
                           cmp=lambda x, y: x[0] - y[0] if x[0] != y[0] else y[1] - x[1])
        size = len(envelopes)
        if size < 2:
            return size
        dp_array = list()
        for index in range(size):
            width, height = envelopes[index]
            low, high = 0, len(dp_array)-1
            while (low <= high):
                mid = (high+low) / 2
                if dp_array[mid][1] < height:
                    low = mid+1
                else:
                    high = mid-1
            if (low) < len(dp_array):
                dp_array[low] = envelopes[index]
            else:
                dp_array.append([width, height])
        return len(dp_array)

    def maxEnvelopesSlow(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # Sort by width
        envelopes.sort(key = lambda x: x[0])
        size = len(envelopes)
        if size < 2:
            return size
        dp_array = [1] * size
        for index in range(1, size):
            width, height = envelopes[index]
            dp_array[index] += max([0] + [dp_array[_] for _ in range(index) if envelopes[_][0] < width and envelopes[_][1] < height])

        return max(dp_array)

solution = Solution()
data = [[4,5],[4,6],[6,7],[2,3],[1,1]]
print "Expected %d, got %d" % (solution.maxEnvelopesSlow(data), solution.maxEnvelopes(data))

data = [[5,4],[6,4],[6,7],[2,3]]
print "Expected %d, got %d" % (solution.maxEnvelopesSlow(data), solution.maxEnvelopes(data))

data = [[30,50],[12,2],[3,4],[12,15]]
print "Expected %d, got %d" % (solution.maxEnvelopesSlow(data), solution.maxEnvelopes(data))

data = [[1,2],[2,3],[3,4],[3,5],[4,5],[5,5],[5,6],[6,7],[7,8]]
print "Expected %d, got %d" % (solution.maxEnvelopesSlow(data), solution.maxEnvelopes(data))


data = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
print "Expected %d, got %d" % (solution.maxEnvelopesSlow(data), solution.maxEnvelopes(data))
