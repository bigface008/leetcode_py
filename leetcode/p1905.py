from typing import List, Set, Tuple

import utils


# dfs()
# if visited -> false
# if g2 not 1 -> false
# if g1 not 1 -> false
# if dfs(neighor)

# dfs() called on g2 == 1
# - not visited
# and g1 == 1
# and check all 1 neighor:
#    and dfs(neighbor)

# https://leetcode.com/problems/count-sub-islands/?envType=daily-question&envId=2024-08-28
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        M, N = len(grid1), len(grid1[0])
        visited = [[False for _ in range(N)] for _ in range(M)]
        # included = [[False for _ in range(N)] for _ in range(M)]

        def justVisit(r: int, c: int):
            visited[r][c] = True
            if r + 1 < M and grid2[r + 1][c] == 1:
                if not visited[r + 1][c]:
                    justVisit(r + 1, c)
            if r - 1 >= 0 and grid2[r - 1][c] == 1:
                if not visited[r - 1][c]:
                    justVisit(r - 1, c)
            if c + 1 < N and grid2[r][c + 1] == 1:
                if not visited[r][c + 1]:
                    justVisit(r, c + 1)
            if c - 1 >= 0 and grid2[r][c - 1] == 1:
                if not visited[r][c - 1]:
                    justVisit(r, c - 1)

        def isIncluded(r: int, c: int):
            visited[r][c] = True
            if grid1[r][c] != 1:
                justVisit(r, c)
                return False
            if r + 1 < M and grid2[r + 1][c] == 1:
                if not visited[r + 1][c] and not isIncluded(r + 1, c):
                    justVisit(r, c)
                    return False
            if r - 1 >= 0 and grid2[r - 1][c] == 1:
                if not visited[r - 1][c] and not isIncluded(r - 1, c):
                    justVisit(r, c)
                    return False
            if c + 1 < N and grid2[r][c + 1] == 1:
                if not visited[r][c + 1] and not isIncluded(r, c + 1):
                    justVisit(r, c)
                    return False
            if c - 1 >= 0 and grid2[r][c - 1] == 1:
                if not visited[r][c - 1] and not isIncluded(r, c - 1):
                    justVisit(r, c)
                    return False
            justVisit(r, c)
            return True

        ans = 0
        for r in range(M):
            for c in range(N):
                if grid2[r][c] == 1 and grid1[r][c] == 1 and not visited[r][c]:
                    if isIncluded(r, c):
                        ans += 1
        return ans


# class Solution:
#     def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
#         M, N = len(grid1), len(grid1[0])
#         visited = [[False for _ in range(N)] for _ in range(M)]
#         included = [[False for _ in range(N)] for _ in range(M)]
#
#         def fillWithRes(r: int, c: int, res: bool):
#             included[r][c] = res
#             visited[r][c] = True
#             if r + 1 < M and grid2[r + 1][c] == 1:
#                 if not visited[r + 1][c]:
#                     fillWithRes(r + 1, c, res)
#             if r - 1 >= 0 and grid2[r - 1][c] == 1:
#                 if not visited[r - 1][c]:
#                     fillWithRes(r - 1, c, res)
#             if c + 1 < N and grid2[r][c + 1] == 1:
#                 if not visited[r][c + 1]:
#                     fillWithRes(r, c + 1, res)
#             if c - 1 >= 0 and grid2[r][c - 1] == 1:
#                 if not visited[r][c - 1]:
#                     fillWithRes(r, c - 1, res)
#
#         def isIncluded(r: int, c: int):
#             visited[r][c] = True
#             if grid1[r][c] != 1:
#                 fillWithRes(r, c, False)
#                 return False
#             if r + 1 < M and grid2[r + 1][c] == 1:
#                 if not visited[r + 1][c] and isIncluded(r + 1, c):
#                     fillWithRes(r + 1, c, False)
#                     return False
#             if r - 1 >= 0 and grid2[r - 1][c] == 1:
#                 if not visited[r - 1][c] and isIncluded(r - 1, c):
#                     fillWithRes(r - 1, c, False)
#                     return False
#             if c + 1 < N and grid2[r][c + 1] == 1:
#                 if not visited[r][c + 1] and isIncluded(r, c + 1):
#                     fillWithRes(r, c + 1, False)
#                     return False
#             if c - 1 >= 0 and grid2[r][c - 1] == 1:
#                 if not visited[r][c - 1] and isIncluded(r, c - 1):
#                     fillWithRes(r, c - 1, False)
#                     return False
#             fillWithRes(r, c, True)
#             return True
#
#         ans = 0
#         for r in range(M):
#             for c in range(N):
#                 if grid2[r][c] == 1 and grid1[r][c] == 1 and not visited[r][c]:
#                     if isIncluded(r, c):
#                         ans += 1
#         return ans


# class Solution:
#     def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
#         M, N = len(grid1), len(grid1[0])
#         visited = [[False for _ in range(N)] for _ in range(M)]
#         included = [[False for _ in range(N)] for _ in range(M)]
#
#         def dfs(r: int, c: int):
#             if visited[r][c]:
#                 return
#             visited[r][c] = True
#             inc = grid1[r][c] == 1
#             if r + 1 < M and grid2[r + 1][c] == 1:
#                 if grid1[r + 1][c] == 0:
#                     inc = False
#                 dfs(r + 1, c)
#             if r - 1 >= 0 and grid2[r - 1][c] == 1:
#                 if grid1[r - 1][c] == 0:
#                     inc = False
#                 dfs(r - 1, c)
#             if c + 1 < N and grid2[r][c + 1] == 1:
#                 if grid1[r][c + 1] == 0:
#                     inc = False
#                 dfs(r, c + 1)
#             if c - 1 >= 0 and grid2[r][c - 1] == 1:
#                 if grid1[r][c - 1] == 0:
#                     inc = False
#                 dfs(r, c - 1)
#             included[r][c] = inc
#
#         ans = 0
#         for r in range(M):
#             for c in range(N):
#                 if grid2[r][c] == 1 and grid1[r][c] == 1 and not visited[r][c]:
#                     dfs(r, c)
#                     if included[r][c]:
#                         ans += 1
#         return ans


# class Solution:
#     def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
#         M, N = len(grid1), len(grid1[0])
#         visited = [[False for _ in range(N)] for _ in range(M)]
#
#         def dfs(r: int, c: int) -> bool:
#             if visited[r][c]:
#                 return False
#             visited[r][c] = True
#             if grid1[r][c] != 1:
#                 return False
#             if r + 1 < M and grid2[r + 1][c] == 1:
#                 if not visited[r + 1][c] and not dfs(r + 1, c):
#                     return False
#             if r - 1 >= 0 and grid2[r - 1][c] == 1:
#                 if not visited[r - 1][c] and not dfs(r - 1, c):
#                     return False
#             if c + 1 < N and grid2[r][c + 1] == 1:
#                 if not visited[r][c + 1] and not dfs(r, c + 1):
#                     return False
#             if c - 1 >= 0 and grid2[r][c - 1] == 1:
#                 if not visited[r][c - 1] and not dfs(r, c - 1):
#                     return False
#             return True
#
#         ans = 0
#         for r in range(M):
#             for c in range(N):
#                 if grid2[r][c] == 1 and grid1[r][c] == 1:
#                     if dfs(r, c):
#                         ans += 1
#         return ans


def tst(grid1: List[List[int]], grid2: List[List[int]], expect: int):
    output = Solution().countSubIslands(grid1, grid2)
    utils.tst(f'count sub islands grid1={grid1} grid2={grid2}', output, expect)


if __name__ == '__main__':
    tst([[1, 1, 1, 0, 0],
         [0, 1, 1, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0],
         [1, 1, 0, 1, 1]],
        [[1, 1, 1, 0, 0],
         [0, 0, 1, 1, 1],
         [0, 1, 0, 0, 0],
         [1, 0, 1, 1, 0],
         [0, 1, 0, 1, 0]], 3)
    tst([[1, 0, 1, 0, 1],
         [1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1],
         [1, 0, 1, 0, 1]],
        [[0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1],
         [0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0],
         [1, 0, 0, 0, 1]], 2)

# class Solution:
# def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
#     M, N = len(grid1), len(grid1[0])
#     visited = [[False for _ in range(N)] for _ in range(M)]
#
#     def dfs(r: int, c: int) -> bool:
#         if visited[r][c]:
#             return False
#         visited[r][c] = True
#         if grid1[r][c] != 1:
#             return False
#         if r + 1 < M and grid2[r + 1][c] == 1:
#             # if grid1[r + 1][c] != 1:
#             #     return False
#             if not visited[r + 1][c] and not dfs(r + 1, c):
#                 return False
#         if r - 1 >= 0 and grid2[r - 1][c] == 1:
#             # if grid1[r - 1][c] != 1:
#             #     return False
#             if not visited[r - 1][c] and not dfs(r - 1, c):
#                 return False
#         if c + 1 < N and grid2[r][c + 1] == 1:
#             # if grid1[r][c + 1] != 1:
#             #     return False
#             if not visited[r][c + 1] and not dfs(r, c + 1):
#                 return False
#         if c - 1 >= 0 and grid2[r][c - 1] == 1:
#             # if grid1[r][c - 1] != 1:
#             #     return False
#             if not visited[r][c - 1] and not dfs(r, c - 1):
#                 return False
#         return True
#
#     ans = 0
#     for r in range(M):
#         for c in range(N):
#             if grid2[r][c] == 1:
#                 if dfs(r, c):
#                     ans += 1
#     return ans
