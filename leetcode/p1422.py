# https://leetcode.com/problems/maximum-score-after-splitting-a-string/?envType=daily-question&envId=2025-01-01
class Solution:
    def maxScore(self, s: str) -> int:
        N = len(s)
        one_cnt = [0] * N
        one_cnt[0] = int(s[0])
        for i in range(1, N):
            one_cnt[i] = one_cnt[i - 1] + int(s[i])
        ans = 0
        for i in range(N - 1):
            left = (i + 1) - one_cnt[i]
            right = one_cnt[-1] - one_cnt[i]
            ans = max(ans, left + right)
        return ans