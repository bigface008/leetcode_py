# https://leetcode.cn/problems/largest-magic-square/description/?envType=daily-question&envId=2026-01-18
from itertools import accumulate
from typing import List, Optional


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        row_pre_sum = [list(accumulate(grid[r], initial=0)) for r in range(M)]
        col_pre_sum = [list(accumulate(list(grid[r][c] for r in range(M)), initial=0)) for c in range(N)]
        mx_edge = 1
        for r in range(M):
            for c in range(N):
                for edge in range(mx_edge + 1, min(M - r, N - c) + 1):
                    group_sum: Optional[int] = None
                    valid = True
                    diagonal_sum_1 = 0
                    diagonal_sum_2 = 0
                    for i in range(edge):
                        curr_row_sum = row_pre_sum[r + i][c + edge] - row_pre_sum[r + i][c]
                        if group_sum is None:
                            group_sum = curr_row_sum
                        elif group_sum != curr_row_sum:
                            valid = False
                            break
                        curr_col_sum = col_pre_sum[c + i][r + edge] - col_pre_sum[c + i][r]
                        if group_sum != curr_col_sum:
                            valid = False
                            break
                        diagonal_sum_1 += grid[r + i][c + i]
                        diagonal_sum_2 += grid[r + i][c + edge - i - 1]
                    if valid and diagonal_sum_1 == diagonal_sum_2 == group_sum:
                        mx_edge = edge
        return mx_edge

        # M, N = len(grid), len(grid[0])
        # mx_edge = 1
        # for r in range(M):
        #     for c in range(N):
        #         for edge in range(mx_edge + 1, min(M - r, N - c) + 1):
        #             # check rows
        #             group_sum: Optional[int] = None
        #             valid = True
        #             diagonal_sum_1 = 0
        #             diagonal_sum_2 = 0
        #             for i in range(edge):
        #                 curr_row_sum = sum(grid[r + i][c + j] for j in range(edge))
        #                 if group_sum is None:
        #                     group_sum = curr_row_sum
        #                 elif group_sum != curr_row_sum:
        #                     valid = False
        #                     break
        #                 curr_col_sum = sum(grid[r + j][c + i] for j in range(edge))
        #                 if group_sum != curr_col_sum:
        #                     valid = False
        #                     break
        #                 diagonal_sum_1 += grid[r + i][c + i]
        #                 diagonal_sum_2 += grid[r + i][c + edge - i - 1]
        #             if valid and diagonal_sum_1 == diagonal_sum_2 == group_sum:
        #                 mx_edge = edge
        # return mx_edge


if __name__ == '__main__':
    print(Solution().largestMagicSquare([[7, 1, 4, 5, 6], [2, 5, 1, 6, 4], [1, 5, 4, 3, 2], [1, 2, 7, 3, 4]]))
