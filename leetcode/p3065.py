# https://leetcode.cn/problems/minimum-operations-to-exceed-threshold-value-i/?envType=daily-question&envId=2025-01-14
import heapq
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        ans = 0
        while nums and nums[0] < k:
            heapq.heappop(nums)
            ans += 1
        return ans