# https://leetcode.com/problems/maximum-number-of-balloons/description/?envType=daily-question&envId=2026-06-22
from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ch_cnt = Counter(text)
        # balloon
        # ban 1 ll oo 2
        return min(ch_cnt.get('b', 0), ch_cnt.get('a', 0), ch_cnt.get('n', 0), ch_cnt.get('l', 0) // 2, ch_cnt.get('o', 0) // 2)