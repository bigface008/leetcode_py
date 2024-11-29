# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/
from functools import cache
from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        N = len(nums)

        prev_lis = [0] * N
        post_lds = [0] * N
        prev_lis[0] = 1
        post_lds[-1] = 1
        for i in range(1, N):
            curr = nums[i]
            res = 1
            for j in range(0, i):
                if nums[j] < curr:
                    res = max(res, prev_lis[j] + 1)
            prev_lis[i] = res
            # prev_lis[i] = max(res, prev_lis[i - 1])

        for i in range(N - 2, -1, -1):
            curr = nums[i]
            res = 1
            for j in range(i + 1, N):
                if nums[j] < curr:
                    res = max(res, post_lds[j] + 1)
            post_lds[i] = res
            # post_lds[i] = max(res, post_lds[i + 1])

        print(f'prev_lis={prev_lis} post_lds={post_lds}')
        return N - max(v1 + v2 - 1 for v1, v2 in zip(prev_lis, post_lds) if v1 != 1 and v2 != 1)
