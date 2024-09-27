from functools import cache
from typing import List


# https://leetcode.com/problems/extra-characters-in-a-string/?envType=daily-question&envId=2024-09-23
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        mxl = max(len(wd) for wd in dictionary)
        dic = set(dictionary)
        N = len(s)

        @cache
        def dfs(i: int) -> int:
            if i == N:
                return 0
            left = i
            ans = 0
            for right in range(i, min(N, i + mxl)):
                wd = s[left:right + 1]
                if wd in dic:
                    ans = max(ans, dfs(right + 1) + len(wd))
            ans = max(ans, dfs(i + 1))
            return ans

        return N - dfs(0)
