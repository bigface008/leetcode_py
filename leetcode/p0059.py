# https://leetcode.cn/problems/spiral-matrix-ii/?envType=daily-question&envId=2025-02-07
from typing import List

import utils


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        r, c = 0, 0
        val = 1
        width, height = n, n
        while width > 0 and height > 0:
            for _ in range(width - 1):
                ans[r][c] = val
                c += 1
                val += 1
            for _ in range(height - 1):
                ans[r][c] = val
                r += 1
                val += 1
            for _ in range(width - 1):
                ans[r][c] = val
                c -= 1
                val += 1
            for _ in range(height - 2):
                ans[r][c] = val
                r -= 1
                val += 1
            ans[r][c] = val
            val += 1
            width -= 2
            height -= 2
            c += 1
        return ans


def check(n: int, expect: List[List[int]]):
    output = Solution().generateMatrix(n)
    utils.tst(f'n={n}', output, expect)


if __name__ == '__main__':
    check(3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]])
