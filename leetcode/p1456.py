# https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
from typing import List, Dict, Tuple


class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        def is_vowel(ch: str) -> bool:
            return ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'

        # freq: Dict[str, int] = dict()
        times = 0
        for i in range(k):
            if i < k and is_vowel(s[i]):
                times += 1
        ans = times
        N = len(s)
        for i in range(k, N):
            if is_vowel(s[i]):
                times += 1
            if is_vowel(s[i-k]):
                times -= 1
            ans = max(ans, times)
        return ans