from math import inf
from functools import cache


# https://leetcode.com/problems/longest-palindromic-subsequence/
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            if i > j:
                return 0
            if i == j:
                return 1
            if s[i] == s[j]:
                return dfs(i + 1, j - 1) + 2
            else:
                return max(dfs(i + 1, j), dfs(i, j - 1))

        return dfs(0, len(s) - 1)