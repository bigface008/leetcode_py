# https://leetcode.cn/problems/find-the-longest-semi-repetitive-substring/
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        left = 0
        repetitive_cnt = 0
        ans = 0
        for right, ch in enumerate(s):
            if right - 1 >= left and ch == s[right - 1]:
                repetitive_cnt += 1
            while left <= right and repetitive_cnt > 1:
                lch = s[left]
                if left + 1 <= right and lch == s[left + 1]:
                    repetitive_cnt -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    print(Solution().longestSemiRepetitiveSubstring("4411794"))
