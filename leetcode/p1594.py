# https://leetcode.cn/problems/maximum-non-negative-product-in-a-matrix/?envType=daily-question&envId=2026-03-23
from typing import List, Tuple, Dict
from math import inf
from functools import cache


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        MOD = pow(10, 9) + 7

        @cache
        def dfs(i: int, j: int) -> Tuple[int, int]:
            val = grid[i][j]
            if i == 0 and j == 0:
                return val, val
            mn, mx = inf, -inf
            if i - 1 >= 0:
                a, b = dfs(i - 1, j)
                a *= val
                b *= val
                mn, mx = min(a, b), max(a, b)
            if j - 1 >= 0:
                a, b = dfs(i, j - 1)
                a *= val
                b *= val
                mn, mx = min(mn, a, b), max(mx, a, b)
            return mn, mx

        _, mx = dfs(M - 1, N - 1)
        if mx < 0:
            return -1
        return mx % MOD


if __name__ == "__main__":
    print(Solution().maxProductPath([[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]]))
