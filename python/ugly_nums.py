'''
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
'''

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return self.isUgly(-1 * num)
        while num > 1:
            if (num % 2 == 0):
                num /= 2
            elif (num % 3 == 0):
                num /= 3
            elif (num % 5 == 0):
                num /= 5
            else:
                return False
        return True

    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        size = len(primes)
        nums = [1]
        indices = [0] * size
        local_num = [0] * size
        while n > 1:
            local_num = [ primes[index] * nums[indices[index]] for index in range(size) ]
            num = min(local_num)
            for index in range(size):
                if local_num[index] == num:
                    indices[index] += 1
            nums.append(num)
            n -= 1
        return nums[-1]

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [1]
        i2,i3,i5=0,0,0
        while n > 0:
            u2,u3,u5 = nums[i2]*2, nums[i3]*3, nums[i5]*5
            num = min(u2, u3, u5)
            if num == u2:
                i2 += 1
            if num == u3:
                i3 += 1
            if num == u5:
                i5 += 1
            nums.append(num)
            n -= 1
        return num[-1]
