# https://leetcode.cn/problems/champagne-tower/description/?envType=daily-question&envId=2026-02-14
from typing import List


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        curr = [float(poured)]
        for i in range(query_row):
            nxt = [0.0] * (i + 2)
            for j, x in enumerate(curr):
                if x > 1:
                    nxt[j] += (x - 1) / 2
                    nxt[j + 1] += (x - 1) / 2
            curr = nxt
        return min(1.0, curr[query_glass])
