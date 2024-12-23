# https://leetcode.cn/problems/maximum-spending-after-buying-items/?envType=daily-question&envId=2024-12-12
import heapq
from typing import List


class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        M, N = len(values), len(values[0])
        min_heap = []
        for i in range(M):
            heapq.heappush(min_heap, (values[i][-1], i, N - 1))
        ans = 0
        day = 1
        while min_heap:
            val, row, col = min_heap[0]
            heapq.heappop(min_heap)
            ans += val * day
            day += 1
            if col != 0:
                heapq.heappush(min_heap, (values[row][col - 1], row, col - 1))
        return ans