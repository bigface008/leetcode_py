# https://leetcode.cn/problems/divide-an-array-into-subarrays-with-minimum-cost-i/?envType=daily-question&envId=2026-02-01
from typing import List
from math import inf


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min_1 = inf
        min_2 = inf
        N = len(nums)
        for i in range(1, N):
            x = nums[i]
            if x < min_1:
                min_2 = min_1
                min_1 = x
            elif x < min_2:
                min_2 = x
        return nums[0] + min_1 + min_2
