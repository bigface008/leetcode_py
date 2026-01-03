# https://leetcode.cn/problems/four-divisors/?envType=daily-question&envId=2026-01-04
from typing import List, Set


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def valid(x: int) -> List[int]:
            if x == 1 or x == 2 or x == 3:
                return []
            factors: List[int] = [1, x]
            d = 2
            while d * d <= x:
                if x % d == 0:
                    factors.append(d)
                    if x != d * d:
                        factors.append(x // d)
                    if len(factors) > 4:
                        return []
                d += 1
            return factors

        ans = 0
        for x in nums:
            factors = valid(x)
            if len(factors) == 4:
                ans += sum(factors)
        return ans


if __name__ == '__main__':
    print(Solution().sumFourDivisors([21, 4, 7]))
