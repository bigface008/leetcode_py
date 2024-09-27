import collections
import copy
from collections import defaultdict
from typing import List

import utils


# https://leetcode.com/problems/rotting-oranges/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        fresh = 0
        dq = collections.deque()
        for i in range(M):
            for j in range(N):
                x = grid[i][j]
                if x == 1:
                    fresh += 1
                elif x == 2:
                    dq.append((i, j))

        ans = -1
        dxs, dys = (1, -1, 0, 0), (0, 0, 1, -1)
        while dq:
            size = len(dq)
            for _ in range(size):
                x, y = dq.popleft()
                for dx, dy in zip(dxs, dys):
                    x1 = x + dx
                    y1 = y + dy
                    if 0 <= x1 < M and 0 <= y1 < N and grid[x1][y1] == 1:
                        fresh -= 1
                        grid[x1][y1] = 2
                        dq.append((x1, y1))
            ans += 1
        return max(ans, 0) if fresh == 0 else -1

        # ans = 0
        # max_time = 0
        # M, N = len(grid), len(grid[0])
        # dxs, dys = (1, -1, 0, 0), (0, 0, 1, -1)
        #
        # rotten_mp = defaultdict(dict)
        #
        # for i in range(M):
        #     for j in range(N):
        #         if grid[i][j] == 2:
        #             for dx, dy in zip(dxs, dys):
        #                 r1, c1 = dx + i, dy + j
        #                 if 0 <= r1 < M and 0 <= c1 < N and grid[r1][c1] == 1:
        #                     rotten_mp[i][j] = collections.deque([(i, j, 0)])
        #                     break
        #
        # all_rotten = False
        # max_time = 0
        # while not all_rotten:
        #     all_rotten = True
        #     for r, row in rotten_mp.items():
        #         for c, dq in row.items():
        #             if dq:
        #                 size = len(dq)
        #                 all_rotten = False
        #                 # print(f'replacing r={r} c={c} dq={dq} max_time={max_time} rotten_mp={rotten_mp}')
        #                 for i in range(size):
        #                     r1, c1, t1 = dq.popleft()
        #                     max_time = max(max_time, t1)
        #                     for dx, dy in zip(dxs, dys):
        #                         r2, c2 = dx + r1, dy + c1
        #                         if 0 <= r2 < M and 0 <= c2 < N and grid[r2][c2] == 1:
        #                             grid[r2][c2] = 2
        #                             dq.append((r2, c2, t1 + 1))
        #                     # print(f'  after replacing r={r} c={c} dq={dq} max_time={max_time} rotten_mp={rotten_mp}')
        #                     # for i in range(M):
        #                     #     print(' ', grid[i])
        #     # print('===================')
        # for i in range(M):
        #     for j in range(N):
        #         if grid[i][j] == 1:
        #             return -1
        # return max_time


def tst(grid: List[List[int]], expect: int):
    g = copy.deepcopy(grid)
    output = Solution().orangesRotting(grid)
    utils.tst(f'oranges rotting in grid={g}', output, expect)


# 2 1 1
# 1 1 0
# 0 1 1

if __name__ == '__main__':
    # tst([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4)
    tst([
        [2, 2, 1, 1, 1, 1],
        [0, 0, 2, 0, 1, 0],
        [2, 0, 0, 0, 2, 2],
        [0, 2, 1, 0, 1, 0],
        [2, 0, 1, 2, 1, 2],
        [0, 0, 2, 1, 0, 0],
        [2, 1, 1, 2, 2, 1]
    ], 3)

    # for i in range(M):
    #     for j in range(N):
    #         if grid[i][j] == 2:
    #             dq = collections.deque()
    #             dq.append((i, j, 0))
    #             while dq:
    #                 r, c, t = dq.popleft()
    #                 max_time = max(max_time, t)
    #                 for dx, dy in zip(dxs, dys):
    #                     r1, c1 = dx + r, dy + c
    #                     if 0 <= r1 < M and 0 <= c1 < N:
    #                         v = grid[r1][c1]
    #                         if v == 0:
    #                             continue
    #                         elif v == 1:
    #                             grid[r1][c1] = 2
    #                             dq.append((r1, c1, t + 1))
    # for i in range(M):
    #     for j in range(N):
    #         if grid[i][j] == 1:
    #             return -1
    # return max_time
