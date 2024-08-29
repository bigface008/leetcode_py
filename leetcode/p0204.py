# https://leetcode.com/problems/count-primes/
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        is_primes = [1] * n
        is_primes[0] = is_primes[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if is_primes[i]:
                for j in range(i * i, n, i):
                    is_primes[j] = 0
        return sum(is_primes)


class Solution3:
    def countPrimes(self, n: int) -> int:
        is_prime = [True] * n
        primes = []
        ans = 0
        for i in range(2, n):
            if is_prime[i]:
                primes.append(i)
            j = 0
            while j < len(primes) and i * primes[j] < n:
                is_prime[j] = False
                if primes[j] % i == 0:
                    break
                j += 1
        return len(primes)


class Solution2:
    def countPrimes(self, n: int) -> int:
        is_prime = [True] * n
        ans = 0
        for i in range(2, n):
            if is_prime[i]:
                ans += 1
                if i * i < n:
                    for j in range(i * i, n, i):
                        is_prime[j] = False
        return ans
