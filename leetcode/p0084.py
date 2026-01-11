# https://leetcode.cn/problems/largest-rectangle-in-histogram/
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        min_stk = [-1]
        heights.append(-1)
        ans = heights[0]
        for right, h in enumerate(heights):
            while len(min_stk) > 1 and heights[min_stk[-1]] >= h:
                mid = min_stk.pop()
                left = min_stk[-1]
                ans = max(ans, heights[mid] * (right - left - 1))
            min_stk.append(right)
        return ans

        # N = len(heights)
        # min_stk = []
        # left = [0] * N
        # right = [N] * N
        # for i, h in enumerate(heights):
        #     while min_stk and heights[min_stk[-1]] >= h:
        #         right_idx = min_stk.pop()
        #         right[right_idx] = i
        #     if min_stk:
        #         left[i] = min_stk[-1]
        #     min_stk.append(i)
        # return max(heights[i] * (right[i] - left[i] - 1) for i in range(N))

        # N = len(heights)
        # min_stk = []
        # max_area = [0] * N
        # for i, h in enumerate(heights):
        #     while min_stk and heights[min_stk[-1]] >= h:
        #         j = min_stk[-1]
        #         max_area[j] += heights[j] * (i - j - 1)
        #         min_stk.pop()
        #     wl = (i - min_stk[-1] - 1) if min_stk else i
        #     max_area[i] = h + wl * h
        #     min_stk.append(i)
        # for i in min_stk:
        #     max_area[i] += heights[i] * (N - 1 - i)
        # return max(max_area)