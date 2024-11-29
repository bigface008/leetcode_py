from typing import List
from functools import cache


# https://leetcode.cn/problems/house-robber-ii/
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)

        @cache
        def dfs(idx: int, last: bool) -> int:
            if idx < 0:
                return 0
            if idx == N - 1:
                if last:
                    return dfs(idx - 2, True) + nums[idx]
                else:
                    return dfs(idx - 1, False)
            if idx == 0:
                return 0 if last else nums[0]
            return max(dfs(idx - 1, last), dfs(idx - 2, last) + nums[idx])

        return max(dfs(N - 1, True), dfs(N - 1, False))
