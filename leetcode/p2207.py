# https://leetcode.cn/problems/maximize-number-of-subsequences-in-a-string/description/?envType=daily-question&envId=2024-09-24
from collections import defaultdict


class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        ch1, ch2 = pattern[0], pattern[1]
        if ch1 == ch2:
            cnt = sum(1 if ch == ch1 else 0 for ch in pattern)
            return cnt * (cnt + 1) // 2

        cnt1, cnt2 = 0, 0
        ans = 0
        for i, ch in enumerate(text):
            if ch == ch1:
                cnt1 += 1
            elif ch == ch2:
                cnt2 += 1
                ans += cnt1
        return ans + max(cnt1, cnt2)


        # ch1, ch2 = pattern[0], pattern[1]
        # ch_to_cnt = defaultdict(int)
        # for i, ch in enumerate(text):
        #     if ch == ch1 or ch == ch2:
        #         ch_to_cnt[ch] += 1
        #
        # if ch1 == ch2:
        #     l = ch_to_cnt[ch1]
        #     return (l + 1) * l // 2
        #
        # cnt1, cnt2 = 0, ch_to_cnt[ch2]
        # ans = max(ch_to_cnt[ch1], ch_to_cnt[ch2])
        # for i, ch in enumerate(text):
        #     if ch == ch1:
        #         cnt1 += 1
        #     elif ch == ch2:
        #         ans += cnt1
        # return ans


if __name__ == '__main__':
    s = "mffiqmrvjmkfmbnaivajzecfdta"
    print(sum(1 if ch == 'h' else 0 for ch in s))
    cnt = 0
    for ch in s:
        if ch == 'h':
            cnt += 1
    print(cnt)