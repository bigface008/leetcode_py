from typing import List
from functools import cache


# https://leetcode.cn/problems/house-robber/
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)

        @cache
        def dfs(idx: int) -> int:
            if idx < 0:
                return 0
            return max(dfs(idx - 1), dfs(idx - 2) + nums[idx])

        return dfs(N - 1)
