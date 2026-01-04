# https://leetcode.cn/problems/maximum-matrix-sum/?envType=daily-question&envId=2026-01-05
from typing import List
import heapq
from math import inf


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ans = 0
        neg_cnt = 0
        min_val = inf
        for row in matrix:
            for x in row:
                if x < 0:
                    neg_cnt += 1
                    x = -x
                min_val = min(min_val, x)
                ans += x
        if neg_cnt % 2 == 0:
            return ans
        else:
            return ans - 2 * min_val


# class Solution:
#     def maxMatrixSum(self, matrix: List[List[int]]) -> int:
#         pq = []  # sum, r1, c1, r2, c2
#         N = len(matrix)
#         res = 0
#         for r in range(N):
#             for c in range(N):
#                 res += matrix[r][c]
#                 if c + 1 < N:
#                     temp = matrix[r][c] + matrix[r][c + 1]
#                     heapq.heappush(pq, (temp, r, c, r, c + 1))
#                 if r + 1 < N:
#                     temp = matrix[r][c] + matrix[r + 1][c]
#                     heapq.heappush(pq, (temp, r, c, r + 1, c))
#         while pq:
#             val, r1, c1, r2, c2 = pq[0]
#             heapq.heappop(pq)
#             if val != matrix[r1][c1] + matrix[r2][c2]:
#                 continue
#             if val > 0:
#                 break
#             res -= 2 * val
#             if r1 - 1 >= 0:
#                 heapq.heappush(pq, (-matrix[r1][c1] + matrix[r1 - 1][c1], r1 - 1, c1, r1, c1))
#                 if r1 == r2:
#                     heapq.heappush(pq, (-matrix[r2][c2] + matrix[r2 - 1][c2], r2 - 1, c2, r2, c2))
#             if r2 + 1 < N:
#                 heapq.heappush(pq, (-matrix[r2][c2] + matrix[r2 + 1][c2], r2, c2, r2 + 1, c2))
#                 if r1 == r2:
#                     heapq.heappush(pq, (-matrix[r1][c1] + matrix[r1 + 1][c1], r1, c1, r1 + 1, c1))
#             if c1 - 1 >= 0:
#                 heapq.heappush(pq, (-matrix[r1][c1] + matrix[r1][c1 - 1], r1, c1 - 1, r1, c1))
#                 if c1 == c2:
#                     heapq.heappush(pq, (-matrix[r2][c2] + matrix[r2][c2 - 1], r2, c2 - 1, r2, c2))
#             if c2 + 1 < N:
#                 heapq.heappush(pq, (-matrix[r2][c2] + matrix[r2][c2 + 1], r2, c2, r2, c2 + 1))
#                 if c1 == c2:
#                     heapq.heappush(pq, (-matrix[r2][c2] + matrix[r2][c2 + 1], r2, c2, r2, c2 + 1))
#             matrix[r1][c1] = -matrix[r1][c1]
#             matrix[r2][c2] = -matrix[r2][c2]
#         return res


if __name__ == '__main__':
    print(Solution().maxMatrixSum([[-1, 0, -1], [-2, 1, 3], [3, 2, 2]]))
    # print(Solution().maxMatrixSum([[1, -1], [-1, 1]]))
