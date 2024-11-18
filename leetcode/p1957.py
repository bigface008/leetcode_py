# https://leetcode.com/problems/delete-characters-to-make-fancy-string/?envType=daily-question&envId=2024-11-01
class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = s[:]
        i = 0
        while i < len(ans):
            ch = ans[i]
            if i + 2 < len(ans) and ch == ans[i + 1] == ans[i + 2]:
                ans = ans[:i] + ans[i + 1:]
            else:
                i += 1
        return ans
