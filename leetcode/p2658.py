# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/?envType=daily-question&envId=2025-01-28
from collections import defaultdict
from typing import List, Tuple

import utils


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        visited = set()
        M, N = len(grid), len(grid[0])

        def dfs(node: Tuple[int, int]) -> int:
            if node in visited:
                return 0
            visited.add(node)
            r, c = node
            res = grid[r][c]
            for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= x < M and 0 <= y < N and ((x, y) not in visited) and grid[x][y] != 0:
                    res += dfs((x, y))
            return res

        ans = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] != 0 and (i, j) not in visited:
                    ans = max(ans, dfs((i, j)))
        return ans


class Solution3:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        parents = defaultdict(tuple)
        ranks = defaultdict(int)
        for r in range(M):
            for c in range(N):
                parents[(r, c)] = (r, c)
                ranks[(r, c)] = 0

        def findParent(node: Tuple[int, int]) -> Tuple[int, int]:
            while node != parents[node]:
                parents[node] = parents[parents[node]]
                node = parents[node]
            return node

        for r in range(M):
            for c in range(N):
                if grid[r][c] != 0:
                    p1 = findParent((r, c))
                    for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                        if 0 <= x < M and 0 <= y < N and grid[x][y] != 0:
                            p2 = findParent((x, y))
                            if p1 == p2:
                                continue
                            if ranks[p1] > ranks[p2]:
                                parents[p2] = p1
                            elif ranks[p1] < ranks[p2]:
                                parents[p1] = p2
                            else:
                                parents[p2] = p1
                                ranks[p1] += 1
        ans = 0
        pa_sum_mp = defaultdict(int)
        for r in range(M):
            for c in range(N):
                if grid[r][c] != 0:
                    pa_sum_mp[parents[(r, c)]] += grid[r][c]
                    ans = max(ans, pa_sum_mp[parents[(r, c)]])
        return ans


class Solution2:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        parents = [[(r, c) for c in range(N)] for r in range(M)]
        ranks = [[0] * N for _ in range(M)]

        def findParent(node: Tuple[int, int]) -> Tuple[int, int]:
            r, c = node
            while node != parents[r][c]:
                parents[r][c] = parents[parents[r][c][0]][parents[r][c][1]]
                node = parents[r][c]
                r, c = node
            return node

        for r in range(M):
            for c in range(N):
                if grid[r][c] != 0:
                    p1 = findParent((r, c))
                    for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                        if 0 <= x < M and 0 <= y < N and grid[x][y] != 0:
                            p2 = findParent((x, y))
                            if p1 == p2:
                                continue
                            if ranks[p1[0]][p1[1]] > ranks[p2[0]][p2[1]]:
                                parents[p2[0]][p2[1]] = p1
                            elif ranks[p1[0]][p1[1]] < ranks[p2[0]][p2[1]]:
                                parents[p1[0]][p1[1]] = p2
                            else:
                                parents[p2[0]][p2[1]] = p1
                                ranks[p1[0]][p1[1]] += 1
        ans = 0
        pa_sum_mp = defaultdict(int)
        for r in range(M):
            for c in range(N):
                if grid[r][c] != 0:
                    pa_sum_mp[parents[r][c]] += grid[r][c]
                    ans = max(ans, pa_sum_mp[parents[r][c]])
        return ans


def check(grid: List[List[int]], expect: int) -> int:
    output = Solution().findMaxFish(grid)
    utils.tst(f'grid={grid}', output, expect)


if __name__ == '__main__':
    # check([[0, 5], [8, 4]], 17)
    check([[0, 0, 10, 8], [4, 1, 8, 0]], 31)
