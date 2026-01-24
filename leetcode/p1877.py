# https://leetcode.cn/problems/minimize-maximum-pair-sum-in-array/?envType=daily-question&envId=2026-01-24
from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        return max(nums[i] + nums[N - i - 1] for i in range(N // 2))