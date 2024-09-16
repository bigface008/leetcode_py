# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts
from collections import defaultdict, Counter
from math import inf

import utils


# It seems that we can use the sliding window. But we have a problem.
# How can we shrink the window? For example, if we have 3 'a' in the current
# window, we cannot directly shrink the window, because maybe we can move right
# pointer by one and get a new 'a', and the condition is actually meet. If we
# shrink the window directly, we will not get the

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        def addCh(mask: int, ch: str) -> int:
            if ch == 'a':
                idx = 0
            elif ch == 'e':
                idx = 1
            elif ch == 'i':
                idx = 2
            elif ch == 'o':
                idx = 3
            elif ch == 'u':
                idx = 4
            else:
                return mask
            return mask ^ (1 << idx)

        mask = 0  # 0 -> even, 1 -> odd
        first_mp = {0: -1}
        ans = 0
        for i, ch in enumerate(s):
            mask = addCh(mask, ch)
            if mask in first_mp:
                ans = max(ans, i - first_mp[mask])
            else:
                first_mp[mask] = i
        return ans


def tst(s: str, expect: int):
    output = Solution().findTheLongestSubstring(s)
    utils.tst(f's={s}', output, expect)


if __name__ == '__main__':
    tst("eleetminicoworoep", 13)
    tst("leetcodeisgreat", 5)
    tst("bcbcbc", 6)
    tst("eeeoo", 4)
