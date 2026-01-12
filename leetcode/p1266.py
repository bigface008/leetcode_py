# https://leetcode.cn/problems/minimum-time-visiting-all-points/description/?envType=daily-question&envId=2026-01-12
from typing import List, Optional, Dict


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        ans = 0
        for i in range(N - 1):
            curr_x, curr_y = points[i]
            next_x, next_y = points[i + 1]
            if curr_x == next_x:
                ans += abs(next_y - curr_y)
            elif curr_y == next_y:
                ans += abs(next_x - curr_x)
            else:
                ans += max(abs(next_x - curr_x), abs(next_y - curr_y))
        return ans