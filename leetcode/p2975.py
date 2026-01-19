# https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/?envType=daily-question&envId=2026-01-16
from itertools import combinations
from typing import List, Set


class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        def f(arr: List[int], mx: int) -> Set[int]:
            arr.append(1)
            arr.append(mx)
            arr.sort()
            return set(abs(x - y) for x, y in combinations(arr, 2))

        MOD = 10 ** 9 + 7
        hf = f(hFences, m)
        vf = f(vFences, n)
        mx_side = max(hf & vf, default=0)
        if mx_side == 0:
            return -1
        return mx_side ** 2 % MOD
