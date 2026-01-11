# https://leetcode.cn/problems/maximal-rectangle/?envType=daily-question&envId=2026-01-11
from typing import List, Dict, Optional


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        N = len(matrix[0])
        heights = [0] * (N + 1)
        ans = 0
        for row in matrix:
            for col, x in enumerate(row):
                if x == '0':
                    heights[col] = 0
                else:
                    heights[col] += 1
            ans = max(ans, self.largestRectangleArea(heights))
        return ans

    def largestRectangleArea(self, heights: List[int]) -> int:
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
