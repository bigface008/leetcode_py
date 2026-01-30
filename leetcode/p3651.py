# https://leetcode.com/problems/minimum-cost-path-with-teleportations/?envType=daily-question&envId=2026-01-28
import heapq
from collections import defaultdict
from typing import List, Dict, Tuple
from math import inf

# 19,36 10,45
# 23,32 13,42
# 16,39 32,23
# 38,17 41,14
# 30,25 36,19
# 53,2  31,24

# 19, 10
# 23, 13
# 16, 32
# 38, 41
# 30, 36
# 53, 31

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])
        grid_val_to_pairs: Dict[int, List[Tuple[int, int]]] = defaultdict(list)
        for i in range(M):
            for j in range(N):
                grid_val_to_pairs[grid[i][j]].append((i, j))
        grid_values = list(grid_val_to_pairs.keys())
        grid_values.sort()
        dp: List[List[List[int]]] = [[[inf] * (k + 1) for _ in range(N)] for _ in range(M)]
        dp[0][0][0] = 0
        for i in range(M):
            for j in range(N):
                for used_jump in range(k + 1):
                    res = inf
                    val = grid[i][j]
                    if i - 1 >= 0:
                        res = min(res, dp[i - 1][j][used_jump] + val)
                    if j - 1 >= 0:
                        res = min(res, dp[i][j - 1][used_jump] + val)
                    if used_jump != 0:
                        for r in range(M):
                            for c in range(N):
                                if r == i and c == j:
                                    continue
                                if grid[r][c] >= val:
                                    res = min(res, dp[r][c][used_jump - 1])
                    dp[i][j][used_jump] = min(res, dp[i][j][used_jump])
        return min(dp[M - 1][N - 1])

# class Solution:
#     def minCost(self, grid: List[List[int]], k: int) -> int:
#         M, N = len(grid), len(grid[0])
#         grid_val_to_pairs: Dict[int, List[Tuple[int, int]]] = defaultdict(list)
#         for i in range(M):
#             for j in range(N):
#                 grid_val_to_pairs[grid[i][j]].append((i, j))
#         grid_values = list(grid_val_to_pairs.keys())
#         grid_values.sort()
#         dp: List[List[List[int]]] = [[[inf] * (k + 1) for _ in range(N)] for _ in range(M)]
#         dp[0][0][0] = 0
#         for i in range(M):
#             for j in range(N):
#                 for used_jump in range(k + 1):
#                     res = inf
#                     val = grid[i][j]
#                     if i - 1 >= 0:
#                         res = min(res, dp[i - 1][j][used_jump] + val)
#                     if j - 1 >= 0:
#                         res = min(res, dp[i][j - 1][used_jump] + val)
#                     if used_jump != 0:
#                         for r in range(i + 1):
#                             for c in range(j + 1):
#                                 if r == i and c == j:
#                                     break
#                                 if grid[r][c] >= val:
#                                     res = min(res, dp[r][c][used_jump - 1])
#                     dp[i][j][used_jump] = min(res, dp[i][j][used_jump])
#         return min(dp[M - 1][N - 1])

        # dp[i][j][remain_skip_time]

        # M, N = len(grid), len(grid[0])
        # grid_val_to_pairs: Dict[int, List[Tuple[int, int]]] = defaultdict(list)
        # for i in range(M):
        #     for j in range(N):
        #         grid_val_to_pairs[grid[i][j]].append((i, j))
        # grid_values = list(grid_val_to_pairs.keys())
        # grid_values.sort()
        #
        # pq = [(0, 0, 0, k)]  # d, r, c, remain_skip_time
        # min_dist = [[inf] * N for _ in range(M)]
        # min_dist[0][0] = 0
        # while pq:
        #     dist, row, col, remain_skip_time = pq[0]
        #     heapq.heappop(pq)
        #     if dist > min_dist[row][col]:
        #         continue
        #     val = grid[row][col]
        #     if row + 1 < M:
        #         neighbor_dist = grid[row + 1][col] + dist
        #         if neighbor_dist < min_dist[row + 1][col]:
        #             min_dist[row + 1][col] = neighbor_dist
        #             heapq.heappush(pq, (neighbor_dist, row + 1, col, remain_skip_time))
        #     if col + 1 < N:
        #         neighbor_dist = grid[row][col + 1] + dist
        #         if neighbor_dist < min_dist[row][col + 1]:
        #             min_dist[row][col + 1] = neighbor_dist
        #             heapq.heappush(pq, (neighbor_dist, row, col + 1, remain_skip_time))
        #     if remain_skip_time > 0:
        #         for grid_val in grid_values:
        #             if grid_val > grid[row][col]:
        #                 break
        #             for r, c in grid_val_to_pairs[grid_val]:
        #                 if r == row and c == col:
        #                     continue
        #                 neighbor_dist = dist
        #                 if neighbor_dist < min_dist[r][c]:
        #                     min_dist[r][c] = neighbor_dist
        #                     heapq.heappush(pq, (neighbor_dist, r, c, remain_skip_time - 1))
        # return min_dist[-1][-1]

        # M, N = len(grid), len(grid[0])
        # pair_arr = []
        # for i in range(M):
        #     for j in range(N):
        #         pair_arr.append((i, j))
        # pair_arr.sort(key=lambda p: grid[p[0]][p[1]])
        # val_seq = [[0] * N for _ in range(M)]
        # for i, (r, c) in enumerate(pair_arr):
        #     val_seq[r][c] = i
        #
        # pq = [(0, 0, 0, k)]  # d, r, c, remain_skip_time
        # min_dist = [[inf] * N for _ in range(M)]
        # while pq:
        #     dist, row, col, remain_skip_time = pq[0]
        #     heapq.heappop(pq)
        #     if dist > min_dist[row][col]:
        #         continue
        #     if row + 1 < M:
        #         neighbor_dist = grid[row + 1][col] + dist
        #         if neighbor_dist < min_dist[row + 1][col]:
        #             min_dist[row + 1][col] = neighbor_dist
        #             heapq.heappush(pq, (neighbor_dist, row + 1, col, remain_skip_time))
        #     if col + 1 < N:
        #         neighbor_dist = grid[row][col + 1] + dist
        #         if neighbor_dist < min_dist[row][col + 1]:
        #             min_dist[row][col + 1] = neighbor_dist
        #             heapq.heappush(pq, (neighbor_dist, row, col + 1, remain_skip_time))
        #     if remain_skip_time > 0:
        #         for seq in range(val_seq[row][col]):
        #             r, c = pair_arr[seq]
        #             neighbor_dist = dist
        #             if neighbor_dist < min_dist[r][c]:
        #                 min_dist[r][c] = neighbor_dist
        #                 heapq.heappush(pq, (neighbor_dist, r, c, remain_skip_time - 1))
        # return min_dist[-1][-1]


if __name__ == '__main__':
    print(Solution().minCost([[19, 10], [23, 13], [16, 32], [38, 41], [30, 36], [53, 31]], 1))
    # print(Solution().minCost([[1, 3, 3], [2, 5, 4], [4, 3, 5]], 2))
