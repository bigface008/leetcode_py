# https://leetcode.cn/problems/length-of-the-longest-alphabetical-continuous-substring/?envType=daily-question&envId=2024-09-19
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        left = 0
        N = len(s)
        ans = 1
        for right in range(1, N):
            x = s[right]
            if ord(x) - 1 == ord(s[right - 1]):
                ans = max(ans, right - left + 1)
            else:
                left = right
        return ans