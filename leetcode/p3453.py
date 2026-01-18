# https://leetcode.com/problems/separate-squares-i/?envType=daily-question&envId=2026-01-13
from typing import List
from math import inf


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        start, end, total = inf, -inf, 0
        for x, y, l in squares:
            start = min(start, y)
            end = max(end, y + l)
            total += l * l

        def check(y_line: float) -> bool:
            area_below = 0
            for x, y, l in squares:
                if y < y_line:
                    area_below += min(y_line - y, l) * l
            return area_below >= total / 2

        max_y = end
        for _ in range((max_y * 10000).bit_length()):
            mid = (start + end) / 2
            if check(mid):
                end = mid
            else:
                start = mid
        return (start + end) / 2