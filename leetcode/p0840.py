# https://leetcode.com/problems/magic-squares-in-grid/?envType=daily-question&envId=2025-12-30
from typing import List, Optional, Tuple


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        magic = [0] * 15
        ans = 0
        for i in range(M - 2):
            for j in range(N - 2):
                # print(f'i={i}, j={j}')
                # print(grid[i][j] + grid[i + 1][j] + grid[i + 2][j])
                # print(grid[i][j + 1] + grid[i + 1][j + 1] + grid[i + 2][j + 1])
                # print(grid[i][j + 2] + grid[i + 1][j + 2] + grid[i + 2][j + 2])
                # print(sum(grid[i][j : j + 3]))
                # print(sum(grid[i + 1][j : j + 3]))
                # print(sum(grid[i + 2][j : j + 3]))
                # print(grid[i][j] + grid[i + 2][j + 2] + grid[i + 1][j + 1])
                # print(grid[i][j + 2] + grid[i + 2][j] + grid[i + 1][j + 1])
                if (grid[i][j] + grid[i + 1][j] + grid[i + 2][j]) != 15 or \
                        (grid[i][j + 1] + grid[i + 1][j + 1] + grid[i + 2][j + 1]) != 15 or \
                        (grid[i][j + 2] + grid[i + 1][j + 2] + grid[i + 2][j + 2]) != 15 or \
                        sum(grid[i][j : j + 3]) != 15 or sum(grid[i + 1][j : j + 3]) != 15 or sum(grid[i + 2][j : j + 3]) != 15 or \
                        not ((grid[i][j] + grid[i + 2][j + 2] + grid[i + 1][j + 1]) == (grid[i][j + 2] + grid[i + 2][j] + grid[i + 1][j + 1]) == 15):
                    continue
                valid = True
                for r in range(3):
                    for c in range(3):
                        x = grid[i + r][j + c]
                        magic[x - 1] += 1
                for k in range(9):
                    if magic[k] != 1:
                        valid = False
                        break
                if valid:
                    ans += 1
                for k in range(15):
                    magic[k] = 0
        return ans


if __name__ == '__main__':
    print(Solution().numMagicSquaresInside(
        [[3, 2, 9, 2, 7], [6, 1, 8, 4, 2], [7, 5, 3, 2, 7], [2, 9, 4, 9, 6], [4, 3, 8, 2, 5]]))
    # print(Solution().numMagicSquaresInside([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]))
