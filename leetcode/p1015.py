# https://leetcode.com/problems/smallest-integer-divisible-by-k/?envType=daily-question&envId=2025-11-25

# x % k == 0
# x = 10 ** 0 + 10 ** 1 + 10 ** 2 + ... + 10 ** n-1
# 10x = 10 ** 1 + 10 ** 2 + xxx + 10 ** n
# 9x = 10 ** n - 1
# x = (10 ** n - 1) // 9

# (10 ** n - 1) // 9 % k == 0
# (10 ** n - 1) = 9 * k * T
# 9 * k * T + 1 = 10 ** n


# k=10 last 0 -x-> 9
# k=11 99+1=100 n=2
# k=..2 8 -x-> 9
# k=..3 ..7 * 7 -> 9

# k2 * 10 + 3 = k
# k2 * 90 + 27 = 9k
# k2 * 90 * 7 + 27 * 7 = 63k


# m = 10 * m_last + 1
# m % k = ((10 * m_last % k) + 1 % k) % k
# = (((10 % k) * (m_last % k)) % k) + 1 % k) % k

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        seen = set()
        x = 1 % k
        n = 1
        while x != 0 and x not in seen:
            seen.add(x)
            x = (10 * x + 1) % k
            n += 1
        if x != 0:
            return -1
        else:
            return n


