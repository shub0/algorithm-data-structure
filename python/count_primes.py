#! /usr/bin/python

'''
Count the number of prime numbers less than a non-negative number, n.
'''

class Solution:
    def isPrime(self, n):
        import math
        max_factor = int(math.sqrt(n)) + 1
        for factor in range(2, max_factor+1):
            if n % factor == 0:
                return False
        return True

    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        primes = [2]
        for curr_number in range(3, n):
            if self.isPrime(curr_number):
                primes.append(curr_number)
        print primes
        return len(primes)

    def sieve_eratosthenes(self, n):
        if n < 2:
            return 0
        is_prime = [True] * (n-1)
        is_prime[0] = False      # 1 is not a prime
        for num in range(2, n-1):
            if not is_prime[num-1]:
                continue
            for index in range(num*num-1, n-1, num):
                is_prime[index] = False
        return len(filter(lambda x: x, is_prime))

if __name__ == '__main__':
    solution = Solution()
    print solution.countPrimes(100)
    print solution.sieve_eratosthenes(3)
