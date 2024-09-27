import collections
from typing import List

import utils


# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        M, N = len(maze), len(maze[0])
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        dq = collections.deque()
        dq.append((entrance[0], entrance[1], 0))
        cnt = 0

        def is_target(r: int, c: int) -> bool:
            if (not (entrance[0] == r and entrance[1] == c)) and (r == 0 or r == M - 1 or c == 0 or c == N - 1):
                return True
            else:
                return False

        while dq:
            r, c, d = dq.popleft()
            maze[r][c] = '+'
            for x, y in zip(dx, dy):
                r1, c1 = r + x, c + y
                if 0 <= r1 < M and 0 <= c1 < N and maze[r1][c1] == '.':
                    if is_target(r1, c1):
                        return d + 1
                    dq.append((r1, c1, d + 1))
                    maze[r1][c1] = '+'
            # if r > 0 and maze[r - 1][c] == '.':
            #     if is_target(r - 1, c):
            #         return cnt + 1
            #     dq.append((r - 1, c))
            # if r < M - 1 and maze[r + 1][c] == '.':
            #     if is_target(r + 1, c):
            #         return cnt + 1
            #     dq.append((r + 1, c))
            # if c > 0 and maze[r][c - 1] == '.':
            #     if is_target(r, c - 1):
            #         return cnt + 1
            #     dq.append((r, c - 1))
            # if c < N - 1 and maze[r][c + 1] == '.':
            #     if is_target(r, c + 1):
            #         return cnt + 1
            #     dq.append((r, c + 1))
        return -1


# class Solution:
#     def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
#         M, N = len(maze), len(maze[0])
#         dq = collections.deque()
#         dq.append((entrance[0], entrance[1]))
#         cnt = 0
#
#         def is_target(r: int, c: int) -> bool:
#             if (not (entrance[0] == r and entrance[1] == c)) and (r == 0 or r == M - 1 or c == 0 or c == N - 1):
#                 return True
#             else:
#                 return False
#
#         while dq:
#             size = len(dq)
#             for _ in range(size):
#                 r, c = dq.popleft()
#                 maze[r][c] = '+'
#                 if r > 0 and maze[r - 1][c] == '.':
#                     if is_target(r - 1, c):
#                         return cnt + 1
#                     dq.append((r - 1, c))
#                 if r < M - 1 and maze[r + 1][c] == '.':
#                     if is_target(r + 1, c):
#                         return cnt + 1
#                     dq.append((r + 1, c))
#                 if c > 0 and maze[r][c - 1] == '.':
#                     if is_target(r, c - 1):
#                         return cnt + 1
#                     dq.append((r, c - 1))
#                 if c < N - 1 and maze[r][c + 1] == '.':
#                     if is_target(r, c + 1):
#                         return cnt + 1
#                     dq.append((r, c + 1))
#             cnt += 1
#         return -1


def tst(maze: List[List[str]], entrance: List[int], expect: int):
    output = Solution().nearestExit(maze, entrance)
    utils.tst(f'nearest exit maze={maze}, entrance={entrance}', output, expect)


if __name__ == '__main__':
    # tst([["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], [1, 2], 1)
    tst([["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0], 2)
