from typing import List
from functools import cache
from math import inf


# https://leetcode.com/problems/min-cost-climbing-stairs/
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dfs(i: int):
            if i < 0:
                return inf
            if i == 0 or i == 1:
                return 0
            return min(dfs(i - 1) + cost[i - 1], dfs(i - 2) + cost[i - 2])

        return dfs(len(cost))