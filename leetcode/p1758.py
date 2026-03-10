# https://leetcode.cn/problems/minimum-changes-to-make-alternating-binary-string/description/?envType=daily-question&envId=2026-03-05
from typing import List, Dict, Tuple, Optional


class Solution:
    def minOperations(self, s: str) -> int:
        zero_start_cnt, one_start_cnt = 0, 0
        N = len(s)
        for i, ch in enumerate(s):
            if i % 2 == 0:
                if ch == '1':
                    zero_start_cnt += 1
                else:
                    one_start_cnt += 1
            else:
                if ch == '1':
                    one_start_cnt += 1
                else:
                    zero_start_cnt += 1
        return min(one_start_cnt, zero_start_cnt)

