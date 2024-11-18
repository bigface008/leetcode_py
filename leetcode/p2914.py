from math import inf


# https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/description/?envType=daily-question&envId=2024-11-05
class Solution:
    def minChanges(self, s: str) -> int:
        cnt1 = 0
        ans = 0
        for i, ch in enumerate(s):
            if ch == '1':
                cnt1 += 1
            if i % 2 == 1 and cnt1 % 2 != 0:
                ans += 1
                cnt1 += 1
        return ans


class Solution2:
    def minChanges(self, s: str) -> int:
        N = len(s)
        cnt0, cnt1 = 0, 0
        for x in s:
            if x == '1':
                cnt1 += 1
            else:
                cnt0 += 1

        left_cnt0, left_cnt1 = 0, 0
        ans = inf
        for i, x in enumerate(s):
            if x == '1':
                left_cnt1 += 1
            else:
                left_cnt0 += 1
            if i % 2 == 1:
                right_cnt1 = cnt1 - left_cnt1
                right_cnt0 = cnt0 - left_cnt0
                l0r1 = left_cnt1 + right_cnt0
                l1r0 = left_cnt0 + right_cnt1
                ans = min(ans, min(l0r1, l1r0))
        return ans
