# https://leetcode.com/problems/number-of-substrings-with-only-1s/?envType=daily-question&envId=2025-11-16
import utils
from typing import Dict, List, Tuple
from collections import defaultdict


class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        ans = 0
        N = len(s)
        i = 0
        while i < N:
            one_cnt = 0
            while i < N and s[i] == '1':
                one_cnt += 1
                i += 1
            if one_cnt != 0:
                ans += (1 + one_cnt) * one_cnt // 2
                ans %= MOD
            i += 1
        return ans


if __name__ == '__main__':
    Solution().numSub('0110111')
