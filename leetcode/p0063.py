# https://leetcode.cn/problems/unique-paths-ii/?envType=daily-question&envId=2025-02-08
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        pass
        # dp[i][j]
        #   if grid[i][j] == 1
        #     = 0
        #   else:
        #     dp[i - 1][j] + dp[i][j - 1]

        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                    elif i == 0:
                        dp[i][j] = dp[i][j - 1]
                    elif j == 0:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]