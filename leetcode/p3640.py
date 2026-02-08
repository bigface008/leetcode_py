# https://leetcode.cn/problems/trionic-array-ii/?envType=daily-question&envId=2026-02-04
from itertools import accumulate
from typing import List, Dict, Tuple


class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        pre_sum = list(accumulate(nums, initial=0))
        N = len(nums)
        i = 0
        descend_ranges: List[Tuple[int, int]] = []
        while i < N:
            start = i
            while i + 1 < N and nums[i] > nums[i + 1]:
                i += 1
            if i > 0 and nums[i - 1] > nums[i]:
                end = i
                descend_ranges.append((start, end))
            i += 1

