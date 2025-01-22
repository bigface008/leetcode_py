# https://leetcode.com/problems/grid-game/?envType=daily-question&envId=2025-01-21
import heapq
from itertools import accumulate
from typing import List
from math import inf

import utils


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        N = len(grid[0])
        row1_sum = sum(grid[0])
        row2_sum = 0
        ans = inf
        for i in range(N):
            row1_sum -= grid[0][i]
            ans = min(ans, max(row1_sum, row2_sum))
            row2_sum += grid[1][i]
        return ans


        # pre_sum = [list(accumulate(row, initial=0)) for row in grid]
        # max1 = 0
        # i1 = -1
        # for i in range(N):
        #     temp = pre_sum[0][i + 1] + pre_sum[1][-1] - pre_sum[1][i]
        #     if temp > max1:
        #         max1 = temp
        #         i1 = i

        # ans = 0
        # for i in range(N):
        #     if i == i1:
        #         continue
        #     if i < i1:
        #         ans = max(ans, pre_sum[1][i1] - pre_sum[1][i])
        #     else:
        #         ans = max(ans, pre_sum[0][i + 1] - pre_sum[0][i1 + 1])
        # return ans


# class Solution:
#     def gridGame(self, grid: List[List[int]]) -> int:
#         N = len(grid[0])
#         dist = [[inf] * N for _ in range(2)]
#         dist[0][0] = grid[0][0]
#         prev = [[None] * N for _ in range(2)]
#         pq = [(grid[0][0], 0, 0)]  # w, r, c
#         while pq:
#             w, r, c = heapq.heappop(pq)
#             for x, y in ((r + 1, c), (r, c + 1)):
#                 if 0 <= x < 2 and 0 <= y < N:
#                     new_w = w + grid[x][y]
#                     if new_w < dist[x][y]:
#                         dist[x][y] = new_w
#                         prev[x][y] = (r, c)
#                         heapq.heappush(pq, (new_w, x, y))
#         r, c = 1, N - 1
#         while not (r == 0 and c == 0):
#             grid[r][c] = 0
#             r, c = prev[r][c]
#
#         # 2
#         dist = [[0] * N for _ in range(2)]
#         dist[0][0] = 0
#         pq = [(0, 0, 0)]  # w, r, c
#         while pq:
#             w, r, c = heapq.heappop(pq)
#             w = -w
#             for x, y in ((r + 1, c), (r, c + 1)):
#                 if 0 <= x < 2 and 0 <= y < N:
#                     new_w = w + grid[x][y]
#                     if new_w > dist[x][y]:
#                         dist[x][y] = new_w
#                         heapq.heappush(pq, (-new_w, x, y))
#         return dist[-1][-1]


def check(grid: List[List[int]], expect: int):
    output = Solution().gridGame(grid)
    utils.tst(f'grid={grid}', output, expect)


if __name__ == '__main__':
    check([[2, 5, 4], [1, 5, 1]], 4)
