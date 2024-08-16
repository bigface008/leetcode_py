from typing import List
from functools import cache


# https://leetcode.com/problems/target-sum/
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        tg = sum(nums) + target
        if tg < 0 or tg % 2 == 1:
            return 0
        tg /= 2
        N = len(nums)

        @cache
        def dfs(i: int, tg: int):
            if i < 0:
                return 1 if tg == 0 else 0
            if tg < nums[i]:
                return dfs(i - 1, tg)
            return dfs(i - 1, tg) + dfs(i - 1, tg - nums[i])

        return dfs(N - 1, tg)
