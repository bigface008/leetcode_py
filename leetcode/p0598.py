# https://leetcode.cn/problems/range-addition-ii/?envType=daily-question&envId=2025-02-02
from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        row_cnt, col_cnt = m, n
        for a, b in ops:
            row_cnt = min(row_cnt, a)
            col_cnt = min(col_cnt, b)
        return row_cnt * col_cnt
