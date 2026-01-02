# https://leetcode.cn/problems/count-negative-numbers-in-a-sorted-matrix/?envType=daily-question&envId=2025-12-28
from typing import List, Dict, Tuple, Optional


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        i, j = 0, N - 1
        ans = 0
        while i < M and j >= 0:
            if grid[i][j] > 0:
                i += 1
            else:
                ans += M - i
                j -= 1
        return ans

# class Solution:
#     def countNegatives(self, grid: List[List[int]]) -> int:
#         ans = 0
#         M, N = len(grid), len(grid[0])
#         prev_end = M
#         for col in range(N):
#             start, end = 0, prev_end
#             while start < end:
#                 mid = (end - start) // 2 + start
#                 if grid[mid][col] < 0:
#                     end = mid
#                 else:
#                     start = mid + 1
#             if start == prev_end:
#                 ans += M - start
#                 continue
#             if grid[start][col] < 0:
#                 start -= 1
#             prev_end = start + 1
#             ans += M - start - 1
#         return ans


if __name__ == '__main__':
    print(Solution().countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
    # print(Solution().countNegatives([[3, 2], [1, 0]]))
