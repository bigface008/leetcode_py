# https://leetcode.cn/problems/minimum-number-of-taps-to-open-to-water-a-garden/
from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = [(i - r, i + r) for i, r in enumerate(ranges)]
        intervals.sort(key=lambda i: i[0])
