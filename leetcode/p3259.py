from typing import List
from functools import cache


# https://leetcode.cn/problems/maximum-energy-boost-from-two-drinks/?envType=daily-question&envId=2024-11-01
class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        N = len(energyDrinkA)
        dp1 = energyDrinkA[0]
        dp0 = energyDrinkB[0]
        for time in range(1, N):
            new_dp1 = max(dp1 + energyDrinkA[time], dp0)
            new_dp0 = max(dp0 + energyDrinkB[time], dp1)
            dp1 = new_dp1
            dp0 = new_dp0
        return max(dp1, dp0)

        # dp = [[0, 0] for _ in range(N)]
        # dp[0][1] = energyDrinkA[0]
        # dp[0][0] = energyDrinkB[0]
        # for time in range(N):
        #     dp[time][1] = max(dp[time - 1][1] + energyDrinkA[time], dp[time - 1][0])
        #     dp[time][0] = max(dp[time - 1][0] + energyDrinkB[time], dp[time - 1][1])
        # return max(dp[N - 1][0], dp[N - 1][1])

        # @cache
        # def dfs(time: int, select_a: bool) -> int:
        #     if time == 1:
        #         if select_a:
        #             return energyDrinkA[0]
        #         else:
        #             return energyDrinkB[0]
        #     if select_a:
        #         return max(dfs(time - 1, True) + energyDrinkA[time - 1], dfs(time - 1, False))
        #     else:
        #         return max(dfs(time - 1, False) + energyDrinkB[time - 1], dfs(time - 1, True))
        #
        # return max(dfs(N, True), dfs(N, False))
