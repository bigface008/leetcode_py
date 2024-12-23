# https://leetcode.cn/problems/largest-rectangle-in-histogram/
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        min_stk = []
        max_area = [0] * N
        for i, h in enumerate(heights):
            while min_stk and heights[min_stk[-1]] >= h:
                j = min_stk[-1]
                max_area[j] += heights[j] * (i - j - 1)
                min_stk.pop()
            wl = (i - min_stk[-1] - 1) if min_stk else i
            max_area[i] = h + wl * h
            min_stk.append(i)
        for i in min_stk:
            max_area[i] += heights[i] * (N - 1 - i)
        return max(max_area)