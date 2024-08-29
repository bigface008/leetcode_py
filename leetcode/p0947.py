from collections import defaultdict
from typing import List

import utils


# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/?envType=daily-question&envId=2024-08-29
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        CNT = len(stones)
        row_dict = defaultdict(set)
        col_dict = defaultdict(set)
        for i, p in enumerate(stones):
            r, c = p
            row_dict[r].add(i)
            col_dict[c].add(i)
        not_visited = set(range(CNT))

        def dfs(i: int):
            r, c = stones[i]
            not_visited.remove(i)
            same_row = row_dict[r]
            for j in same_row:
                if j == i:
                    continue
                if j in not_visited:
                    dfs(j)
            same_col = col_dict[c]
            for j in same_col:
                if j == i:
                    continue
                if j in not_visited:
                    dfs(j)

        part_cnt = 0
        idx = 0
        while not_visited and idx < CNT:
            if idx in not_visited:
                dfs(idx)
                part_cnt += 1
            idx += 1
        return CNT - part_cnt


# class Solution:
#     def removeStones(self, stones: List[List[int]]) -> int:
#         CNT = len(stones)
#         row_dict = defaultdict(set)
#         col_dict = defaultdict(set)
#         for i, p in enumerate(stones):
#             r, c = p
#             row_dict[r].add(i)
#             col_dict[c].add(i)
#         ans = 0
#
#         def dfs(i: int, remove_cnt: int):
#             if i == CNT:
#                 nonlocal ans
#                 ans = max(ans, remove_cnt)
#                 return
#             r, c = stones[i]
#             dfs(i + 1, remove_cnt)
#             if len(row_dict[r]) > 1 or len(col_dict[c]) > 1:
#                 row_dict[r].remove(i)
#                 col_dict[c].remove(i)
#                 dfs(i + 1, remove_cnt + 1)
#                 row_dict[r].add(i)
#                 col_dict[c].add(i)
#
#         dfs(0, 0)
#         return ans


# class Solution:
#     def removeStones(self, stones: List[List[int]]) -> int:
#         CNT = len(stones)
#         M, N = 0, 0
#         for p in stones:
#             r, c = p
#             M = max(M, r + 1)
#             N = max(N, c + 1)
#         # plane = [[0 for _ in range(N)] for _ in range(M)]
#         row_dict = defaultdict(set)
#         col_dict = defaultdict(set)
#         for i, p in enumerate(stones):
#             r, c = p
#             row_dict[r].add(i)
#             col_dict[c].add(i)
#         ans = 0
#
#         def dfs(i: int, remove_cnt: int):
#             if i == CNT:
#                 nonlocal ans
#                 ans = max(ans, remove_cnt)
#                 return
#             r, c = stones[i]
#             if len(row_dict[r]) > 1 or len(col_dict[c]) > 1:
#                 row_dict[r].remove(i)
#                 col_dict[c].remove(i)
#                 dfs(i + 1, remove_cnt + 1)
#                 row_dict[r].add(i)
#                 col_dict[c].add(i)
#             dfs(i + 1, remove_cnt)
#
#         dfs(0, 0)
#         return ans
# def dfs(row: int, remove_cnt: int):
# if row == M:
#     nonlocal ans
#     ans = max(ans, remove_cnt)
#     return
# row_st = row_dict[row]
# ret = 0
# for i in row_st:
#     r, c = stones[i]
#     if len(col_dict[c]) == 1: # can remove
#         dfs()


def tst(stones: List[List[int]], expect: int):
    output = Solution().removeStones(stones)
    utils.tst(f'remove stones stones={stones}', output, expect)


if __name__ == '__main__':
    tst([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]], 5)
    tst([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]], 3)
    tst([[0, 0]], 0)
    tst([[0, 1], [1, 2], [1, 3], [3, 3], [2, 3], [0, 2]], 5)
