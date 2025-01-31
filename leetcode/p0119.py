# https://leetcode.cn/problems/pascals-triangle-ii/description/?envType=daily-question&envId=2025-01-28
from typing import List
from functools import cache


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        N = rowIndex + 1
        dp = [[0] * (row + 1) for row in range(N)]
        dp[0][0] = 1
        for row in range(N):
            for i in range(row + 1):
                if i == 0 or i == row:
                    dp[row][i] = 1
                    continue
                dp[row][i] = dp[row - 1][i - 1] + dp[row - 1][i]
        return dp[-1]

        # @cache
        # def dfs(i: int, row: int) -> int:
        #     if i == 0:
        #         return 1
        #     if i == rowIndex:
        #         return 1
        #     return dfs(i - 1, row - 1) + dfs(i, row - 1)

