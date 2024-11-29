import heapq
from typing import List
from math import inf

import utils


# https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/?envType=daily-question&envId=2024-11-29
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        M, N = len(grid), len(grid[0])
        dpos = ((1, 0), (0, 1), (-1, 0), (0, -1))
        dist = [[inf] * N for _ in range(M)]
        pq = [(0, 0, 0)] # dist, row, col
        while pq:
            d, r, c = heapq.heappop(pq)
            if d > dist[r][c]:
                continue
            if r == M - 1 and c == N - 1:
                return d
            for dx, dy in dpos:
                x, y = r + dx, c + dy
                if 0 <= x < M and 0 <= y < N:
                    new_d = max(d + 1, grid[x][y])
                    new_d += (new_d - x - y) % 2
                    if new_d < dist[x][y]:
                        dist[x][y] = new_d
                        heapq.heappush(pq, (new_d, x, y))
        return -1



def tst(grid: List[List[int]], expect: int):
    output = Solution().minimumTime(grid)
    utils.tst(f'minimumTime {grid}', output, expect)


if __name__ == '__main__':
    tst([[0, 1, 3, 2], [5, 1, 2, 5], [4, 3, 8, 6]], 7)
