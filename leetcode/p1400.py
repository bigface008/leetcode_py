# https://leetcode.com/problems/construct-k-palindrome-strings/?envType=daily-question&envId=2025-01-11
from collections import Counter
from typing import List, Dict

import utils

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        N = len(s)
        cnt = Counter(s)
        odd_cnt = sum(c % 2 for c in cnt.values())
        # odd_cnt = len([cnt for cnt in cnt.values() if cnt % 2 == 1])
        return max(odd_cnt, 1) <= k <= N


class Solution2:
    def canConstruct(self, s: str, k: int) -> bool:
        cnt = Counter(s)

        def dfs(freq: Dict[int, int], K: int) -> bool:
            if K == 1:
                odd_cnt = len([cnt for cnt in freq.values() if cnt % 2 == 1])
                return odd_cnt == 0 or odd_cnt == 1
            for ch in freq.keys():
                temp = freq[ch]
                old = temp
                while temp >= 0:
                    freq[ch] -= 1
                    if dfs(freq, K - 1):
                        return True
                    temp -= 1
                freq[ch] = old
            return False

        return dfs(cnt, k)


def check(s: str, k: int, expect: int):
    output = Solution().canConstruct(s, k)
    utils.tst(f's={s} k={k}', output, expect)


if __name__ == '__main__':
    check('annabelle', 2, True)