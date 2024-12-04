# https://leetcode.cn/problems/minimum-operations-to-reduce-x-to-zero/description/
from math import inf
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        N = len(nums)
        all_sum = sum(nums)
        target = all_sum - x
        if target < 0:
            return -1
        left = 0
        window_sum = 0
        ans = inf
        for right in range(N):
            curr = nums[right]
            window_sum += curr
            while window_sum > target:
                window_sum -= nums[left]
                left += 1
            if window_sum == target:
                ans = min(ans, N - (right - left + 1))
        return ans if ans is not inf else -1