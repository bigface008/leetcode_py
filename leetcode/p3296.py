# https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/?envType=daily-question&envId=2026-03-13
from typing import List, Dict, Tuple, Optional
from math import inf
from functools import cache


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        N = len(workerTimes)
        workerTimes.sort()
        def get_time(diff: int, worker_idx: int) -> int:
            return (1 + diff) * diff // 2 * workerTimes[worker_idx]

        min_arr = workerTimes.copy()
        min_val = inf
        for i in range(N - 1, -1, -1):
            x = workerTimes[i]
            min_val = min(min_val, x)
            min_arr[i] = min_val

        @cache
        def dfs(height: int, idx: int) -> int:
            if height == 0:
                return 0
            if height == 1:
                return min_val[idx]
            if idx == N - 1:
                return get_time(height, idx)

            start, end = 0, height + 1
            while start < end:
                mid = (start + end) // 2
                time = max(get_time(mid, idx), dfs(height - mid, idx + 1))
                if mid + 1 <= height:
                    time_1 = max(get_time(mid, idx), dfs(height - mid, idx + 1))



# class Solution:
#     def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
#         def get_time(diff: int, worker: int) -> int:
#             return (1 + diff) * diff // 2 * worker
#
#         min_arr = workerTimes.copy()
#         min_val = inf
#         for i, x in enumerate(workerTimes):
#             min_val = min(min_val, x)
#             min_arr[i] = min_val
#
#         @cache
#         def dfs(height: int, idx: int) -> int:
#             if height == 0:
#                 # print(f'height: {height} idx: {idx} -> {0}')
#                 return 0
#             if height == 1:
#                 # print(f'height: {height} idx: {idx} -> {min(workerTimes[:idx + 1])}')
#                 return min_arr[idx]
#             if idx == 0:
#                 # print(f'height: {height} idx: {idx} -> {get_time(height, workerTimes[idx])}')
#                 return get_time(height, workerTimes[idx])
#             res = inf
#             for h in range(0, height + 1):
#                 res = min(res, max(get_time(h, workerTimes[idx]), dfs(height - h, idx - 1)))
#             # print(f'height: {height} idx: {idx} -> {res}')
#             return res
#
#         return dfs(mountainHeight, len(workerTimes) - 1)


if __name__ == "__main__":
    print(Solution().minNumberOfSeconds(2, [7, 1]))
    # print(Solution().minNumberOfSeconds(1, [2, 1]))
    # print(Solution().minNumberOfSeconds(4, [2, 1, 1]))
