from typing import List


# https://leetcode.com/problems/palindrome-partitioning/
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []

        def dfs(i: int):
            if i == len(s):
                ans.append(path.copy())
                return

            for j in range(i, len(s)):
                temp = s[i:j + 1]
                if temp == temp[::-1]:
                    path.append(temp)
                    dfs(j + 1)
                    path.pop()

        dfs(0)
        return ans
