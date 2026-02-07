# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/?envType=daily-question&envId=2026-02-07
from typing import List
from math import inf


class Solution:
    def minimumDeletions(self, s: str) -> int:
        N = len(s)
        NA = sum(1 if x == 'a' else 0 for x in s)
        left_a_cnt = 0
        ans = NA
        for i, x in enumerate(s):
            if x == 'a':
                left_a_cnt += 1
            left_b_cnt = i + 1 - left_a_cnt
            right_a_cnt = NA - left_a_cnt
            ans = min(ans, right_a_cnt + left_b_cnt)
        return ans