from typing import List
from functools import cache


# https://leetcode.com/problems/combination-sum-iv/description/
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        N = len(nums)
        nums.sort(reverse=True)

        @cache
        def dfs(tg: int) -> int:
            if tg < 0:
                return 0
            if tg == 0:
                return 1
            res = 0
            for n in nums:
                res += dfs(tg - n)
            return res

        return dfs(target)