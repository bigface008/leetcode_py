# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
import heapq
from typing import List
from math import inf

import utils


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        K = len(nums)
        min_heap = []
        INT_MAX = 1 << 31 - 1
        heap_max = -INT_MAX
        for i, l in enumerate(nums):
            heapq.heappush(min_heap, (l[0], i, 0))
            heap_max = max(heap_max, l[0])
        start, end = -INT_MAX, INT_MAX
        while min_heap:
            val, l_i, i = min_heap[0]
            if len(min_heap) == K:
                if (end - start > heap_max - val) or (val < start and (end - start == heap_max - val)):
                    start = val
                    end = heap_max
            else:
                break
            heapq.heappop(min_heap)
            if i + 1 < len(nums[l_i]):
                x = nums[l_i][i + 1]
                heapq.heappush(min_heap, (x, l_i, i + 1))
                heap_max = max(heap_max, x)
        return [start, end]


def check(nums: List[List[int]], expect: List[int]):
    output = Solution().smallestRange(nums)
    utils.tst(f'nums={nums}', output, expect)


if __name__ == '__main__':
    check([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]], [20, 24])
