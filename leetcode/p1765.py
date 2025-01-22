# https://leetcode.com/problems/map-of-highest-peak/?envType=daily-question&envId=2025-01-22
from collections import deque
from typing import List

import utils


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        M, N = len(isWater), len(isWater[0])
        dq = deque()
        ans = [[-1] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                if isWater[i][j] == 1:
                    dq.append((i, j))
                    ans[i][j] = 0
        while dq:
            r, c = dq.popleft()
            for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= x < M and 0 <= y < N:
                    if ans[x][y] != -1:
                        continue
                    ans[x][y] = ans[r][c] + 1
                    dq.append((x, y))
        return ans


def check(isWater: List[List[int]], expect: List[List[int]]):
    output = Solution().highestPeak(isWater)
    utils.tst(f'isWater={isWater}', output, expect)


if __name__ == '__main__':
    check([[0, 1], [0, 0]], [[1, 0], [2, 1]])
