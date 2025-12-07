# https://leetcode.com/problems/count-number-of-trapezoids-i/description
from typing import List, Dict, Optional, Tuple
from collections import defaultdict


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = pow(10, 9) + 7
        y_to_count: Dict[int, int] = defaultdict(int)
        for i, (_, y) in enumerate(points):
            y_to_count[y] += 1
        N = len(y_to_count)
        acc = 0
        ans = 0
        for i, count in enumerate(y_to_count.values()):
            curr = count * (count - 1) // 2
            if i != 0:
                ans += acc * curr
            acc += curr
        return ans % MOD


