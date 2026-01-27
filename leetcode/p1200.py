# https://leetcode.cn/problems/minimum-absolute-difference/?envType=daily-question&envId=2026-01-26
from collections import defaultdict
from typing import List, Dict, Tuple
from math import inf


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        N = len(arr)
        min_diff = inf
        min_diff_pairs: List[List[int]] = []
        for i in range(N - 1):
            a, b = arr[i], arr[i + 1]
            diff = b - a
            if diff < min_diff:
                min_diff_pairs = [[a, b]]
                min_diff = diff
            elif diff == min_diff:
                min_diff_pairs.append([a, b])
        return min_diff_pairs
