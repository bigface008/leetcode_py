# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/?envType=daily-question&envId=2025-01-04
import string
from collections import Counter

import utils


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        for ch in string.ascii_lowercase:
            li, ri = s.find(ch), s.rfind(ch)
            if li != ri:
                ans += len(set(s[li + 1:ri]))
        return ans


# class Solution:
#     def countPalindromicSubsequence(self, s: str) -> int:
#         N = len(s)
#         cnt = Counter(s)
#         left_cnt = Counter()
#         left_cnt[s[0]] += 1
#         pa_set = set()
#         for i in range(1, N - 1):
#             curr = s[i]
#             for ch, left in left_cnt.items():
#                 left = left_cnt[ch]
#                 right = cnt[ch] - left - (0 if curr != ch else 1)
#                 prev_str = ch + curr
#                 if left != 0 and right != 0 and prev_str not in pa_set:
#                     pa_set.add(prev_str)
#             left_cnt[curr] += 1
#         return len(pa_set)


def check(s: str, expect: int):
    output = Solution().countPalindromicSubsequence(s)
    utils.tst(f'', output, expect)


if __name__ == '__main__':
    check('aabca', 3)
    # check('bbcbaba', 4)
