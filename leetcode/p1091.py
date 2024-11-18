import collections
from typing import List

import utils


# https://leetcode.cn/problems/shortest-path-in-binary-matrix/
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        N = len(grid)
        if N == 1:
            return 1
        dq = collections.deque()
        dq.append((0, 0))
        dxs = (1, 0, -1, 0, 1, 1, -1, -1)
        dys = (0, 1, 0, -1, 1, -1, 1, -1)
        visited = set()
        visited.add((0, 0))
        ans = 1
        while dq:
            size = len(dq)
            for _ in range(size):
                r, c = dq.popleft()
                for dx, dy in zip(dxs, dys):
                    x, y = r + dx, c + dy
                    if 0 <= x < N and 0 <= y < N and (x, y) not in visited and grid[x][y] == 0:
                        if x == N - 1 and y == N - 1:
                            return ans + 1
                        dq.append((x, y))
                        visited.add((x, y))
            ans += 1
        return -1


class Solution2:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        length = len(grid)
        if length == 1:
            return 1
        que = collections.deque()
        visited = {}
        que.appendleft((0,0))
        visited[(0,0)] = True
        start = 1
        while que:
            for _ in range(len(que)):
                ind, con = que.pop()
                for pos_h, pos_v in [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]:
                    new_ind = ind + pos_h
                    new_con = con + pos_v
                    if 0 <= new_ind < length and 0 <= new_con < length and grid[new_ind][new_con] == 0 and not visited.get((new_ind, new_con)):
                        if new_ind == length - 1 and new_con == length - 1:
                            return start + 1
                        que.appendleft((new_ind, new_con))
                        visited[(new_ind, new_con)] = True
            start += 1
        return -1


def tst(grid: List[List[int]], expect: int):
    output = Solution().shortestPathBinaryMatrix(grid)
    utils.tst(f'shortest path binary matrix grid={grid}', output, expect)


if __name__ == '__main__':
    # tst([[0, 1], [1, 0]], 2)
    tst([[0, 0, 0], [1, 1, 0], [1, 1, 0]], 4)
