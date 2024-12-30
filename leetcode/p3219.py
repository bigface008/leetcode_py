# https://leetcode.cn/problems/minimum-cost-for-cutting-cake-ii/?envType=daily-question&envId=2024-12-31
from typing import List


class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        ans = 0
        i, j = 0, 0
        row_cnt, col_cnt = 1, 1
        while i < m - 1 and j < n - 1:
            hc, vc = horizontalCut[i], verticalCut[j]
            if hc >= vc:
                ans += hc * row_cnt
                col_cnt += 1
                i += 1
            else:
                ans += vc * col_cnt
                row_cnt += 1
                j += 1
        while i < m - 1:
            hc = horizontalCut[i]
            ans += hc * row_cnt
            i += 1
        while j < n - 1:
            vc = verticalCut[j]
            ans += vc * col_cnt
            j += 1
        return ans