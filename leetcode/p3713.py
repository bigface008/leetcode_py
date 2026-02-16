# https://leetcode.cn/problems/longest-balanced-substring-i/?envType=daily-question&envId=2026-02-12
from typing import Dict


class Solution:
    def longestBalanced(self, s: str) -> int:
        N = len(s)
        left = 0
        freq_map: Dict[str, int] = dict()
        for right in range(N):
            ch = s[right]
            freq_map[ch] += 1