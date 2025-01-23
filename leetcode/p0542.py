# https://leetcode.com/problems/01-matrix/
from collections import deque
from typing import List

import utils


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        M, N = len(mat), len(mat[0])
        dq = deque()
        ans = [[-1] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                if mat[i][j] == 0:
                    dq.append((i, j))
                    ans[i][j] = 0
        dist = 0
        while dq:
            size = len(dq)
            for _ in range(size):
                r, c = dq.popleft()
                for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= x < M and 0 <= y < N and ans[x][y] == -1:
                        dq.append((x, y))
                        ans[x][y] = dist + 1
            dist += 1
        return ans


def check(mat: List[List[int]], expect: List[List[int]]):
    output = Solution().updateMatrix(mat)
    utils.tst(f'mat={mat}', output, expect)


if __name__ == '__main__':
    check([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [0, 0, 0]])
