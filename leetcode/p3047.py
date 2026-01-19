# https://leetcode.cn/problems/find-the-largest-area-of-square-inside-two-rectangles/?envType=daily-question&envId=2026-01-17
from typing import List


class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        mx_edge = 0
        for i, ((bl_x_i, bl_y_i), (tr_x_i, tr_y_i)) in enumerate(zip(bottomLeft, topRight)):
            for j in range(i):
                bl_x_j, bl_y_j = bottomLeft[j]
                tr_x_j, tr_y_j = topRight[j]
                width = min(tr_x_i, tr_x_j) - max(bl_x_i, bl_x_j)
                height = min(tr_y_i, tr_y_j) - max(bl_y_i, bl_y_j)
                side = min(width, height)
                if side > mx_edge:
                    mx_edge = side
        return mx_edge ** 2
