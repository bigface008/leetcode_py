# https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k
from typing import List, Dict, Tuple


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])
        dp = [[[0] * k for _ in range(N)] for _ in range(M)]
        MOD = pow(10, 9) + 7

        dp[0][0][grid[0][0] % k] = 1
        for j in range(1, N):
            for r in range(k):
                dp[0][j][(r + grid[0][j]) % k] = dp[0][j - 1][r]
        for i in range(1, M):
            for r in range(k):
                dp[i][0][(r + grid[i][0]) % k] = dp[i - 1][0][r]
        for i in range(1, M):
            for j in range(1, N):
                for r in range(k):
                    dp[i][j][(r + grid[i][j]) % k] = (dp[i - 1][j][r] + dp[i][j - 1][r]) % MOD
        return dp[M - 1][N - 1][0]
