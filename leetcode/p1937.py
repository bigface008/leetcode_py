from typing import List
from math import inf
import utils


# dfs(0,j) = points[0][j]
# dfs(i,j) = max(dfs(i-1,k) - abs(j,k) for k in range(N)) + points[i][j]
# k >= j:
#   dfs(i-1,k) - (k - j)
# https://leetcode.com/problems/maximum-number-of-points-with-cost/?envType=daily-question&envId=2024-08-17
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        M = len(points)
        N = len(points[0])
        f = points[0].copy()
        for i in range(1, M):
            preLeftMax, preRightMax = -inf, -inf
            cp = f.copy()
            for j in range(N):
                preLeftMax = max(preLeftMax, cp[j] + j)
                f[j] = max(f[j], points[i][j] - j + preLeftMax)
            for j in range(N - 1, -1, -1):
                preRightMax = max(preRightMax, cp[j] - j)
                f[j] = max(f[j], points[i][j] + j + preRightMax)
        return max(f)



        # f = [[0 for _ in range(N)] for _ in range(M)]
        # for j in range(N):
        #     f[0][j] = points[0][j]
        # for i in range(1, M):
        #     for j in range(N):
        #         f[i][j] = max(f[i - 1][k] - abs(k - j) for k in range(N)) + points[i][j]
        # return max(f[-1])


def tst(points: List[List[int]], expect: int):
    output = Solution().maxPoints(points)
    utils.tst(f'max points={points}', output, expect)


if __name__ == '__main__':
    tst([[1, 2, 3], [1, 5, 1], [3, 1, 1]], 9)
    tst([[1, 5], [2, 3], [4, 2]], 11)
