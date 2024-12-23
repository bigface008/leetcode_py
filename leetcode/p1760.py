# https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/?envType=daily-question&envId=2024-12-07
import heapq
from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        N = len(nums)
        left, right = 1, max(nums)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            ops = 0
            for x in nums:
                ops += (x - 1) // mid
            if ops <= maxOperations:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
