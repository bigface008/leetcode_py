# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/description/?envType=daily-question&envId=2024-11-28
import heapq
from typing import List
from functools import cache
from math import inf

import utils

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dpos = ((0, 1), (0, -1), (1, 0), (-1, 0))

        pq = [(grid[0][0], (0, 0))] # len, pt
        dist = [[inf] * N for _ in range(M)]
        while pq:
            d, pos = heapq.heappop(pq)
            r, c = pos
            if d > dist[r][c]:
                continue
            for dx, dy in dpos:
                x, y = r + dx, c + dy
                if 0 <= x < M and 0 <= y < N:
                    new_d = d + grid[x][y]
                    if new_d < dist[x][y]:
                        dist[x][y] = new_d
                        heapq.heappush(pq, (new_d, (x, y)))
        return dist[-1][-1]




class Solution2:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dpos = ((0, 1), (0, -1), (1, 0), (-1, 0))

        @cache
        def dfs(r: int, c: int) -> int:
            if r == 0 and c == 0:
                return grid[0][0]
            ret = inf
            for dx, dy in dpos:
                x, y = r + dx, c + dy
                if 0 <= x < M and 0 <= y < N:
                    print(f'r={r} c={c} x={x}, y={y}')
                    ret = min(dfs(x, y), ret)
            if grid[r][c] == 1:
                ret += 1
            print(f'r={r}, c={c}, ret={ret}')
            return ret

        return dfs(M - 1, N - 1)


def tst(grid: List[List[int]], expect: int):
    output = Solution().minimumObstacles(grid)
    utils.tst(f'min obstacle grid={grid}', output, expect)


if __name__ == '__main__':
    tst([[0, 1, 1], [1, 1, 0], [1, 1, 0]], 2)
