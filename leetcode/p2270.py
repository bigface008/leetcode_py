# https://leetcode.com/problems/number-of-ways-to-split-array/description/?envType=daily-question&envId=2025-01-03
from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        N = len(nums)
        all_sum = sum(nums)
        left_sum = 0
        ans = 0
        for i, x in enumerate(nums):
            left_sum += x
            right_sum = all_sum - left_sum
            if left_sum >= right_sum and i != N - 1:
                ans += 1
        return ans