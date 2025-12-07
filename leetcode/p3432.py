# https://leetcode.com/problems/count-partitions-with-even-sum-difference
from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        N = len(nums)
        ALL = sum(nums)
        left_sum = 0
        ans = 0
        for i in range(N - 1):
            x = nums[i]
            left_sum += x
            if abs(left_sum - (ALL - left_sum)) % 2 == 0:
                ans += 1
        return ans