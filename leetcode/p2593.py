# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/description/?envType=daily-question&envId=2024-12-13
import heapq
from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        N = len(nums)
        arr = [(x, i) for i, x in enumerate(nums)]
        arr.sort()
        ans = 0
        marked = [False] * N
        marked_cnt = 0
        i = 0
        while marked_cnt != N:
            idx = arr[i][1]
            if marked[idx]:
                i += 1
                continue
            ans += arr[i][0]
            marked[idx] = True
            marked_cnt += 1
            if idx - 1 >= 0 and not marked[idx - 1]:
                marked[idx - 1] = True
                marked_cnt += 1
            if idx + 1 < N and not marked[idx + 1]:
                marked[idx + 1] = True
                marked_cnt += 1
            i += 1
        return ans


        # min_heap = [(x, i) for i, x in enumerate(nums)]
        # heapq.heapify(min_heap)
        # marked = [False] * N
        # marked_cnt = 0
        # ans = 0
        # while marked_cnt != N and min_heap:
        #     x, i = min_heap[0]
        #     heapq.heappop(min_heap)
        #     if marked[i]:
        #         continue
        #
        # return ans