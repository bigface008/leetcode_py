# https://leetcode.com/problems/shortest-palindrome/?envType=daily-question&envId=2024-09-20
from collections import defaultdict

import utils


# aacecaaa
# 01234567
# abcd
# 0123


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        N = len(s)
        if not N:
            return ''

        ns = s + '#' + s[::-1]
        lps = [0] * len(ns)
        length = 0
        i = 1
        while i < len(ns):
            if ns[i] == ns[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length > 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        count = lps[-1]
        return s[count:][::-1] + s
        # ret = []
        # for i in range(lps[-1]):
        #     ret.append(s[-i - 1])
        # ret.extend(s)
        # return ''.join(ret)
        # N = len(s)
        # if not N:
        #     return ''
        # ans = N
        #
        # i = 0
        # ch = s[0]
        # for j in range(N - 1, -1, -1):
        #     if s[j] != ch:
        #         continue
        #     if i == j:
        #         ans = min(ans, (N - i - 1) * 2 + 1 - N)
        #         break
        #     cnt = j - i + 1
        #     mid = (i + j - 1) // 2
        #     k = 1
        #     match = True
        #     k2 = mid
        #     k3 = (i + j + 1) // 2
        #     # while i + k <= mid:
        #     #     if s[i + k] == s[j - k]:
        #     #         k += 1
        #     #     else:
        #     #         match = False
        #     #         break
        #     if match:
        #         if cnt % 2 == 0:
        #             ans = min(ans, (N - (mid + 1)) * 2 - N)
        #         else:
        #             ans = min(ans, (N - (mid + 2)) * 2 + 1 - N)
        #         break
        # ret = []
        # for i in range(ans):
        #     ret.append(s[-i - 1])
        # ret.extend(s)
        # return ''.join(ret)


def tst(s: str, expect: str):
    output = Solution().shortestPalindrome(s)
    utils.tst(f'shortest palindrome s={s}', output, expect)


if __name__ == '__main__':
    tst('aacecaaa', 'aaacecaaa')
    tst('abcd', 'dcbabcd')
