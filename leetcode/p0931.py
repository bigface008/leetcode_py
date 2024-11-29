from typing import List
from functools import cache
from math import inf


# https://leetcode.cn/problems/minimum-falling-path-sum/
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        dp = [[0] * N for _ in range(N)]
        for c in range(N):
            dp[0][c] = matrix[0][c]
        for r in range(1, N):
            for c in range(N):
                ret = inf
                for dy in (-1, 0, 1):
                        y = c + dy
                        if 0 <= y < N:
                            ret = min(ret, dp[r - 1][y])
                dp[r][c] = ret + matrix[r][c]
        return min(dp[-1])

        # @cache
        # def dfs(r: int, c: int) -> int:
        #     x = matrix[r][c]
        #     if r == 0:
        #         return x
        #     ret = inf
        #     for dy in (-1, 0, 1):
        #         y = c + dy
        #         if 0 <= y < N:
        #             ret = min(ret, dfs(r - 1, y))
        #     ret += x
        #     return ret

        # return min(dfs(N - 1, i) for i in range(N))
