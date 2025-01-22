# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/?envType=daily-question&envId=2025-01-18
import heapq
from typing import List
from math import inf


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dpos = ((0, 1), (0, -1), (1, 0), (-1, 0))
        pq = [(0, 0, 0)] # w, r, c
        dist = [[inf] * N for _ in range(M)]
        dist[0][0] = 0
        while pq:
            w, r, c = pq[0]
            heapq.heappop(pq)
            for i, (dx, dy) in enumerate(dpos):
                x, y = r + dx, c + dy
                if 0 <= x < M and 0 <= y < N:
                    new_w = w + (0 if grid[r][c] == i + 1 else 1)
                    if new_w < dist[x][y]:
                        dist[x][y] = new_w
                        heapq.heappush(pq, (new_w, x, y))
        return dist[-1][-1]
