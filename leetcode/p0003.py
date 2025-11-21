# https://leetcode.com/problems/longest-substring-without-repeating-characters/
from collections import Counter

import utils


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        left = 0
        cnt = Counter()
        ans = 1
        for right in range(N):
            ch = s[right]
            cnt[ch] += 1
            while cnt[ch] > 1:
                lch = s[left]
                cnt[lch] -= 1
                if cnt[lch] == 0:
                    del cnt[lch]
                left += 1
            ans = max(ans, right - left + 1)
        return ans

        #     while left <= right:
        #         ch_left = s[left]
        #         cnt[ch_left] -= 1
        #         if cnt[ch_left] == 0:
        #             del cnt[ch_left]
        #         left += 1
        #         valid = True
        #         for k, v in cnt.items():
        #             if v != 1:
        #                 valid = False
        #                 break
        #         if valid:
        #             break
        #     ans = right - left + 1
        # return ans


def check(s: str, expect: int):
    output = Solution().lengthOfLongestSubstring(s)
    utils.tst(f's={s}', output, expect)


if __name__ == '__main__':
    check('abcabcbb', 3)