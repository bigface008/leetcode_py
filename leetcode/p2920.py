# https://leetcode.cn/problems/maximum-points-after-collecting-coins-from-all-nodes/?envType=daily-question&envId=2025-01-23
from typing import List
from functools import cache

import utils


# [[1,0],[0,2],[1,3]]

# 0 -> 1 -> 3
#   -> 2

# [9,3,8,9]


# class Solution:
#     def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
#         N = len(edges) + 1
#         graph = [[] for _ in range(N)]
#         for a, b in edges:
#             graph[a].append(b)
#             graph[b].append(a)
#
#         def dfs(node: int, pa: int, need_half: bool) -> int:
#             coin = coins[node]
#             if need_half:
#                 coin //= 2
#             res1 = coin // 2
#             for child in graph[node]:
#                 if child != pa:
#                     res1 += dfs(child, node, True)
#             # if coin < k:
#             #     print(f'node: {node} need_half: {need_half} coin: {coin} must 1 res: {res1}')
#             #     return res1
#             res2 = coin - k
#             for child in graph[node]:
#                 if child != pa:
#                     res2 += dfs(child, node, need_half)
#             if res1 > res2:
#                 print(f'node: {node} need_half: {need_half} coin: {coin} choose 1 res: {res1}')
#             else:
#                 print(f'node: {node} need_half: {need_half} coin: {coin} choose 2 res: {res2}')
#             return max(res1, res2)
#
#         return dfs(0, -1, False)


class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        N = len(edges) + 1
        graph = [[] for _ in range(N)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        dp = []



# class Solution:
#     def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
#         N = len(edges) + 1
#         graph = [[] for _ in range(N)]
#         for a, b in edges:
#             graph[a].append(b)
#             graph[b].append(a)
#
#         @cache
#         def dfs(node: int, pa: int, half_cnt: int) -> int:
#             coin = coins[node] >> half_cnt
#             res1 = coin >> 1
#             res2 = coin - k
#             for child in graph[node]:
#                 if child != pa:
#                     if half_cnt + 1 < 14:
#                         res1 += dfs(child, node, half_cnt + 1)
#                     res2 += dfs(child, node, half_cnt)
#             return max(res1, res2)
#
#         return dfs(0, -1, 0)


def check(edges: List[List[int]], coins: List[int], k: int, expect: int):
    output = Solution().maximumPoints(edges, coins, k)
    utils.tst(f'edges={edges}, coins={coins}, k={k}', output, expect)


if __name__ == '__main__':
    # check([[0, 1], [1, 2], [2, 3]], [10, 10, 3, 3], 5, 11)
    # check([[1, 0], [0, 2], [1, 3]], [9, 3, 8, 9], 0, 29)
    check([[0, 1], [0, 2], [3, 2], [0, 4]], [5, 6, 8, 7, 4], 7, 8)

    # 0:5 -> 1:6
    #     -> 4:4
    #     -> 2:8 -> 3:7
    #
