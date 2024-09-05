# 假设有个2D的数组代表一个草场，里面的w代表墙，.代表草地，B代表牛的初始位置，*代表终点，牛牛可
# 以上下左右移动，要移动到墙的位置前必须用炸弹炸掉墙，开始有3个炸弹；把炸掉一个墙也算做一步，求
# 最少多少步可以到终点
import heapq
from typing import List
from collections import deque
from math import inf

import utils


def solution(grid: List[str]) -> int:
    M, N = len(grid), len(grid[0])
    row_cow, col_cow = -1, -1
    row_tgt, col_tgt = -1, -1
    ans = inf
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 'B':
                row_cow, col_cow = i, j
            if grid[i][j] == '*':
                row_tgt, col_tgt = i, j
        if row_cow != -1 and row_tgt != -1:
            break

    pq = [(0, row_cow, col_cow, 3)]
    dist = [[inf for _ in range(N)] for _ in range(M)]
    dist[row_cow][col_cow] = 0
    while pq:
        step_cnt, r, c, bomb_cnt = heapq.heappop(pq)
        nbs = []
        if r + 1 < M:
            nbs.append((r + 1, c))
        if r - 1 >= 0:
            nbs.append((r - 1, c))
        if c + 1 < N:
            nbs.append((r, c + 1))
        if c - 1 >= 0:
            nbs.append((r, c - 1))
        for x, y in nbs:
            nb_dist = dist[x][y]
            if grid[x][y] == 'W':
                if bomb_cnt > 0:
                    new_step_cnt = step_cnt + 2
                    if new_step_cnt < nb_dist:
                        dist[x][y] = new_step_cnt
                        heapq.heappush(pq, (new_step_cnt, x, y, bomb_cnt - 1))
            else:
                new_step_cnt = step_cnt + 1
                if new_step_cnt < nb_dist:
                    dist[x][y] = new_step_cnt
                    heapq.heappush(pq, (new_step_cnt, x, y, bomb_cnt))
    return int(dist[row_tgt][col_tgt])

    # bfs
    # visited = [[False for _ in range(N)] for _ in range(M)]
    # dq = deque()
    # dq.append((row_cow, col_cow, 3))
    # while dq:
    #     r, c, bomb_cnt = dq.popleft()
    #     visited[r][c] = True
    #     if r + 1 < M and not visited[r + 1][c]:
    #         if
    #         dq.append((r + 1, c, ))


def tst(grid: List[str], expect: int):
    output = solution(grid)
    utils.tst(f'sol grid={grid}', output, expect)


if __name__ == '__main__':
    tst([
        'B......',
        'WWWWWWW',
        'WWWWWWW',
        'WWWWWW*',
    ], 12)
