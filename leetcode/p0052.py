# https://leetcode.cn/problems/n-queens-ii/description/?envType=daily-question&envId=2024-12-02
class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        M = 2 * n -  1
        col_used = [False] * n
        diag1_used = [False] * M
        diag2_used = [False] * M

        def dfs(row: int) -> int:
            if row == n:
                return 1
            res = 0
            for col in range(n):
                if not col_used[col] and not diag1_used[row + col] and not diag2_used[row - col]:
                    col_used[col] = diag1_used[row + col] = diag2_used[row - col] = True
                    res += dfs(row + 1)
                    col_used[col] = diag1_used[row + col] = diag2_used[row - col] = False
            return res
        return dfs(0)
