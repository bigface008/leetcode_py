# https://leetcode.com/problems/count-vowel-strings-in-ranges/?envType=daily-question&envId=2025-01-02
from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        N = len(words)
        pre_sum = [0] * (N + 1)

        def isVowel(ch: str) -> bool:
            return ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'

        for i, word in enumerate(words):
            pre_sum[i + 1] = pre_sum[i]
            if isVowel(word[0]) and isVowel(word[-1]):
                pre_sum[i + 1] += 1
        Q = len(queries)
        ans = [0] * Q
        for i, (l, r) in enumerate(queries):
            ans[i] = pre_sum[r + 1] - pre_sum[l]
        return ans