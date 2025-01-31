# https://leetcode.com/problems/making-a-large-island/?envType=daily-question&envId=2025-01-31
from typing import List, Tuple
from collections import defaultdict

import utils


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        island_2_size = defaultdict(int)
        island_cnt = 0
        visited = [[-1] * N for _ in range(N)]

        def dfs(node: Tuple[int, int]) -> int:
            r, c = node
            visited[r][c] = island_cnt
            res = 1
            for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= x < N and 0 <= y < N and grid[x][y] == 1 and visited[x][y] == -1:
                    res += dfs((x, y))
            return res

        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1 and visited[r][c] == -1:
                    island_2_size[island_cnt] = dfs((r, c))
                    island_cnt += 1
        if island_cnt == 1:
            return min(N * N, island_2_size[0] + 1)
        ans = 1
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    islands = set()
                    for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                        if 0 <= x < N and 0 <= y < N and visited[x][y] != -1:
                            islands.add(visited[x][y])
                    if len(islands) > 1:
                        ans = max(ans, 1 + sum(island_2_size[i] for i in islands))
        return ans


def check(grid: List[List[int]], expect: int):
    output = Solution().largestIsland(grid)
    utils.tst(f'grid={grid}', output, expect)


if __name__ == '__main__':
    check([[1, 0], [0, 1]], 3)
