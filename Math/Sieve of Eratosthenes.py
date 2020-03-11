# Given a number n, print all primes smaller than or equal to n.
# It is also given that n is a small number (smaller than 10 million)
import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        prime = [True]*(n)
        prime[0] = False
        prime[1] = False
        k = int(math.sqrt(n))+1
        for p in range(2,k):
            if prime[p]:
                for i in range(2*p,n,p):
                    prime[i] = False
        return sum(prime)
