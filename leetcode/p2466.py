from functools import cache


# https://leetcode.cn/problems/count-ways-to-build-good-strings/description/
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = pow(10, 9) + 7

        @cache
        def dfs(l: int) -> int:
            if l > high:
                return 0
            res = 0
            if l >= low:
                res += 1
            res += (dfs(l + zero) + dfs(l + one) % MOD)
            return res % MOD

        return dfs(0)