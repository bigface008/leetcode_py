# https://leetcode.com/problems/trapping-rain-water-ii/?envType=daily-question&envId=2025-01-19
import heapq
from typing import List

import utils


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        M, N = len(heightMap), len(heightMap[0])
        hp = []
        for i, row in enumerate(heightMap):
            for j, h in enumerate(row):
                if i == 0 or i == M - 1 or j == 0 or j == N - 1:
                    hp.append((h, i, j))
                    row[j] = -1
        heapq.heapify(hp)

        ans = 0
        while hp:
            h, i, j = heapq.heappop(hp)
            for x, y in ((i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)):
                if 0 <= x < M and 0 <= y < N and heightMap[x][y] >= 0:
                    ans += max(h - heightMap[x][y], 0)
                    heapq.heappush(hp, (max(h, heightMap[x][y]), x, y))
                    heightMap[x][y] = -1
        return ans




class Solution2:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        M, N = len(heightMap), len(heightMap[0])
        row_height = [[0] * N for _ in range(M)]
        for r in range(M):
            left, right = 0, N - 1
            max_left, max_right = 0, 0
            while left <= right:
                max_left = max(heightMap[r][left], max_left)
                max_right = max(heightMap[r][right], max_right)
                if max_left < max_right:
                    row_height[r][left] = max_left
                    left += 1
                else:
                    row_height[r][right] = max_right
                    right -= 1
        # col_height = [[0] * N for _ in range(M)]
        ans = 0
        for c in range(N):
            left, right = 0, M - 1
            max_left, max_right = 0, 0
            while left <= right:
                max_left = max(heightMap[left][c], max_left)
                max_right = max(heightMap[right][c], max_right)
                if max_left < max_right:
                    row_height[left][c] = min(row_height[left][c], max_left)
                    ans += max(0, row_height[left][c] - heightMap[left][c])
                    # col_height[left][c] = max_left
                    left += 1
                else:
                    row_height[right][c] = min(row_height[right][c], max_right)
                    ans += max(0, row_height[right][c] - heightMap[right][c])
                    # col_height[right][c] = max_right
                    right -= 1
        # ans = 0
        # for r in range(M):
        #     for c in range(N):
        #         ans += min(row_height[r][c], col_height[r][c])
        return ans


def check(heightMap: List[List[int]], expect: int):
    output = Solution().trapRainWater(heightMap)
    utils.tst(f'heightMap={heightMap}', output, expect)


if __name__ == '__main__':
    # check([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]], 4)
    # check([[1, 3, 1], [1, 0, 1], [1, 3, 1]], 1)
    check([[12, 13, 1, 12], [13, 4, 13, 12], [13, 8, 10, 12], [12, 13, 12, 12], [13, 13, 13, 13]], 14)


# 12 13 1  12
# 13 4  13 12
# 13 8  10 12
# 12 13 12 13
# 13 13 13 13


# 8 4 2

# 0  0  0  0
# 0  9  0  0
# 0  4  2  0
# 0  0  1  0
# 0  0  0  0

# 1 3 1
# 1 0 1
# 1 3 1

# 0 0 0
# 0 1 0
# 0 0 0

# 1 3 1
# 1 1 1
# 1 3 1
