# https://leetcode.cn/problems/final-array-state-after-k-multiplication-operations-i/?envType=daily-question&envId=2024-12-13
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        N = len(nums)
        for _ in range(k):
            min_idx = 0
            min_val = nums[0]
            for i in range(1, N):
                if nums[i] < min_val:
                    min_val = nums[i]
                    min_idx = i
            nums[min_idx] *= multiplier
        return nums