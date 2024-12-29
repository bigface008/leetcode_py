# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/?envType=daily-question&envId=2024-12-29
from itertools import count
from typing import List
from functools import cache


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        N = len(words[0])
        M = len(target)
        MOD = pow(10, 9) + 7
        cnt = [[0] * 26 for _ in range(N)]
        for wd in words:
            for i, ch in enumerate(wd):
                cnt[i][ord(ch) - ord('a')] += 1

        @cache
        def dfs(word_pos: int, target_pos: int) -> int:
            if target_pos == M:
                return 1
            if N - word_pos < M - target_pos:
                return 0
            ch = target[target_pos]
            chi = ord(ch) - ord('a')
            temp = cnt[word_pos][chi] * dfs(word_pos + 1, target_pos + 1) + dfs(word_pos + 1, target_pos)
            return temp % MOD

        return dfs(0, 0)