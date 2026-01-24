# https://leetcode.cn/problems/minimum-difference-between-highest-and-lowest-of-k-scores/?envType=daily-question&envId=2026-01-25
from typing import List
from math import inf


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)
        ans = inf
        for i in range(N - k + 1):
            mn, mx = nums[i], nums[i + k - 1]
            ans = min(ans, mx - mn)
        return ans