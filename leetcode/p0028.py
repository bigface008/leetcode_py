# https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/
from typing import List

import utils


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        def get_lps(pattern: str) -> List[int]:
            l = 0
            i = 1
            N = len(needle)
            ans = [0] * N
            while i < N:
                if pattern[i] == pattern[l]:
                    l += 1
                    ans[i] = l
                    i += 1
                else:
                    if l == 0:
                        ans[i] = 0
                        i += 1
                    else:
                        l = ans[l - 1]
            return ans

        N, M = len(haystack), len(needle)
        j = 0
        lps = get_lps(needle)
        for i in range(N):
            while j > 0 and haystack[i] != needle[j]:
                j = lps[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == M:
                return i - M + 1
        return -1


def check(haystack: str, needle: str, expect: int):
    output = Solution().strStr(haystack, needle)
    utils.tst(f'haystack={haystack}, needle={needle}', output, expect)


if __name__ == '__main__':
    # check('sadbutsad', 'sad', 0)
    check('leetcode', 'leeto', -1)
