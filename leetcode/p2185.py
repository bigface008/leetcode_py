# https://leetcode.com/problems/counting-words-with-a-given-prefix/?envType=daily-question&envId=2025-01-09
# from itertools import count
from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return len([w for w in words if w.startswith(pref)])