# https://leetcode.com/problems/rank-transform-of-an-array/?envType=daily-question&envId=2026-07-12
from typing import List, Dict, Set
from sortedcontainers import SortedDict


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        st: Set[int] = set(arr)
        sorted_arr = sorted(list(st))
        value_to_rank: Dict[int, int] = dict()
        for i, x in enumerate(sorted_arr):
            value_to_rank[x] = i + 1
        ans = [0] * len(arr)
        for i, x in enumerate(arr):
            ans[i] = value_to_rank[x]
        return ans