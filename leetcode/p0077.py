from typing import List


# https://leetcode.com/problems/combinations/
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i):
            if len(path) == k:
                ans.append(path.copy())
                return

            for j in range(i, n + 1):
                if n - j + 1 < k:
                    return
                path.append(j)
                dfs(j + 1)
                path.pop()

        dfs(1)
        return ans
