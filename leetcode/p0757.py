# https://leetcode.com/problems/set-intersection-size-at-least-two/?envType=daily-question&envId=2025-11-20
from typing import List, Tuple, Dict, Optional

# 1,2 2,3 -> 3
# 1,3 2,4 -> 2
# 1,4 2,3 -> 2
# 1,2 2,3 3,4 -> 4
# 1,3 2,4 4,5 -> 4


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        N = len(intervals)
        intervals.sort(key=lambda t: (t[1], -t[0]))
        head = [-1, -1]
        res = 0
        for left, right in intervals:
            if head[0] >= left and head[1] <= right:
                continue
            if left > head[1]:
                head = [right - 1, right]
                res += 2
            else:
                head = [head[1], right]
                res += 1
        return res
