from typing import List, Set


# https://leetcode.com/problems/n-queens/
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = [0] * n
        ans = []
        used = [False] * n
        m = 2 * n - 1
        diag1 = [False] * m
        diag2 = [False] * m

        def dfs(r: int):
            if r == n:
                ans.append(['.' * c + 'Q' + '.' * (n - c - 1) for c in cols])
                return
            for c in range(n):
                if not used[c] and not diag1[r + c] and not diag2[r - c]:
                    cols[r] = c
                    used[c] = diag1[r + c] = diag2[r - c] = True
                    dfs(r + 1)
                    used[c] = diag1[r + c] = diag2[r - c] = False

        dfs(0)
        return ans

        # def dfs(r: int, s: Set[int]):
        #     if r == n:
        #         ans.append(['.' * c + 'Q' + '.' * (n - c - 1) for c in cols])
        #         return
        #     for c in s:
        #         if all(r + c != R + cols[R] and r - c != R - cols[R] for R in range(r)):
        #             cols[r] = c
        #             dfs(r + 1, s - {c})
        #
        # dfs(0, set(range(n)))
        # return ans
