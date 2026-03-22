# https://leetcode.cn/problems/get-biggest-three-rhombus-sums-in-a-grid/?envType=daily-question&envId=2026-03-16
from typing import List
from math import inf
import heapq


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        M, N = len(grid), len(grid[0])
        ans: List[int] = []

        for r1 in range(M):
            for c1 in range(N):
                side = 1
                while r1 + side - 1 < M and c1 + side - 1 < N:
                    half = side // 2
                    temp = 0
                    if half != 0:
                        for r in range(r1 + half, r1, -1):
                            c = r1 + half + c1 - r
                            temp += grid[r][c]
                        for r in range(r1, r1 + half):
                            c = r - r1 + (c1 + half)
                            temp += grid[r][c]
                        for r in range(r1 + half + 1, r1 + side):
                            c = r - (r1 + half) + c1
                            temp += grid[r][c]
                        for r in range(r1 + side - 2, r1 + half - 1, -1):
                            c = r1 + side - 1 + c1 + half - r
                            temp += grid[r][c]
                    else:
                        temp = grid[r1][c1]
                    need_add = True
                    for x in ans:
                        if x == temp:
                            need_add = False
                            break
                    if need_add:
                        ans.append(temp)
                        ans.sort(reverse=True)
                        if len(ans) > 3:
                            ans.pop()
                    temp = 0
                    side += 2
        return ans


if __name__ == "__main__":
    # print(Solution().getBiggestThree(
    #     [[3, 4, 5, 1, 3], [3, 3, 4, 2, 3], [20, 30, 200, 40, 10], [1, 5, 5, 4, 1], [4, 3, 2, 2, 5]]))
    print(Solution().getBiggestThree([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
