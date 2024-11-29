from typing import List
from math import inf


# https://leetcode.cn/problems/minimum-falling-path-sum-ii/
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dp = [[0] * N for _ in range(N)]
        pre_min = [inf] * N
        nxt_min = [inf] * N
        for c in range(N):
            x = grid[0][c]
            dp[0][c] = x
            if c + 1 < N:
                pre_min[c + 1] = min(pre_min[c], x)
        for c in range(N - 1, -1, -1):
            x = grid[0][c]
            if c >= 1:
                nxt_min[c - 1] = min(nxt_min[c], x)
        for r in range(1, N):
            for c in range(N):
                dp[r][c] = min(pre_min[c], nxt_min[c]) + grid[r][c]
            pre_min = [inf] * N
            nxt_min = [inf] * N
            for c in range(N):
                if c + 1 < N:
                    pre_min[c + 1] = min(pre_min[c], dp[r][c])
            for c in range(N - 1, -1, -1):
                x = dp[r][c]
                if c >= 1:
                    nxt_min[c - 1] = min(nxt_min[c], dp[r][c])
        return min(dp[-1])
