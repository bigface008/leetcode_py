# https://leetcode.cn/problems/permutation-difference-between-two-strings
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        chToPos = {}
        for i in range(len(s)):
            chToPos[s[i]] = i
        ans = 0
        for i in range(len(t)):
            ans += abs(i - chToPos[t[i]])
        return ans