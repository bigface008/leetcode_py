# https://leetcode.cn/problems/sliding-window-median/
from typing import List
import heapq


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        left = []
        right = []
        start = 0
        for i in range(k):
            x = nums[i]
            if len(left) == len(right):
                right_min, idx = heapq.heappushpop(right, (x, i))
                heapq.heappush(left, (-right_min, idx))
            else:
                left_max, idx = heapq.heappushpop(left, (-x, i))
                heapq.heappush(right, (-left_max, idx))
        mid = 0
        if len(left) == len(right):
            mid = (-left[0] + right[0]) / 2
        else:
            mid = -left[0]
        ans = [mid]

        N = len(nums)
        for end in range(k, N):
            start = end - k





