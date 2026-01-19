# https://leetcode.cn/problems/maximize-area-of-square-hole-in-grid/description/
from typing import List


class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def longestConsecutive(nums: List[int]) -> int:
            st = set(nums)
            mx_side = 1
            for x in st:
                if x + 1 not in st:
                    continue
                y = x
                while y + 1 in st:
                    y += 1
                side = y - x + 1
                mx_side = max(mx_side, side)
            return mx_side

        mx_side = min(longestConsecutive(hBars), longestConsecutive(vBars)) + 1
        return mx_side ** 2

        # def f(arr: List[int]) -> int:
        #     arr.sort()
        #     mx_len = 1
        #     N = len(arr)
        #     i = 0
        #     while i < N:
        #         start = i
        #         while i < N - 1 and arr[i] == arr[i + 1] - 1:
        #             i += 1
        #         curr_len = i - start + 1
        #         mx_len = max(mx_len, curr_len)
        #         i += 1
        #     return mx_len + 1
        #
        # mx_side = min(f(hBars), f(vBars))
        # return mx_side ** 2

