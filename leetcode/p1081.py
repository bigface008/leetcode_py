# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/?envType=daily-question&envId=2026-07-19
from typing import List, Dict, Set
from collections import Counter


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        left_cnt = Counter(s)
        ans: List[str] = []
        in_ans: Set[str] = set()
        for ch in s:
            left_cnt[ch] -= 1
            if ch in in_ans:
                continue
            while ans and ch < ans[-1] and left_cnt[ans[-1]] > 0:
                in_ans.remove(ans.pop())
            ans.append(ch)
            in_ans.add(ch)
        return "".join(ans)