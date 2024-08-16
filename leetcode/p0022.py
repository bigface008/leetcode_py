from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        m = 2 * n
        ans = []
        path = ['' for i in range(m)]

        def dfs(i: int, open: int):
            if i == m:
                ans.append(''.join(path))
                return
            if open < n:
                path[i] = '('
                dfs(i + 1, open + 1)
            if i - open < open:
                path[i] = ')'
                dfs(i + 1, open)

        dfs(0, 0)
        return ans