# https://leetcode.cn/problems/minimum-operations-to-exceed-threshold-value-ii/?envType=daily-question&envId=2025-01-15
import heapq
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        ans = 0
        while len(nums) >= 2 and nums[0] < k:
            ans += 1
            a = nums[0]
            heapq.heappop(nums)
            b = nums[0]
            # heapq.heappop(nums)
            # heapq.heappush(nums, min(a, b) * 2 + max(a, b))
            heapq.heapreplace(nums, min(a, b) * 2 + max(a, b))
        return ans
