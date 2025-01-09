# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/?envType=daily-question&envId=2025-01-08
from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        N = len(words)
        ans = 0
        for i in range(N):
            wi = words[i]
            for j in range(i + 1, N):
                wj = words[j]
                if i == j or len(wj) < len(wi):
                    continue
                if wj.startswith(wi) and wj.endswith(wi):
                    ans += 1
        return ans