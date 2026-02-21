# https://leetcode.cn/problems/prime-number-of-set-bits-in-binary-representation/?envType=daily-question&envId=2026-02-21
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:

        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            i = 2
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 1
            return True

        ans = 0
        for x in range(left, right + 1):
            if is_prime(x.bit_count()):
                ans += 1
        return ans