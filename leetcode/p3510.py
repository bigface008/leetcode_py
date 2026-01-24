# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/?envType=daily-question&envId=2026-01-23
import heapq
from typing import List


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        hq = [] # (sum, start, end)
        N = len(nums)
        invalid_pair_cnt = 0
        for i in range(N - 1):
            a, b = nums[i], nums[i + 1]
            if a > b:
                invalid_pair_cnt += 1
            heapq.heappush(hq, (a + b, i, i + 1))

        left = list(range(-1, N + 1))

        while invalid_pair_cnt != 0 and hq:
            pair_sum, start, end = hq[0]
            heapq.heappop(hq)


