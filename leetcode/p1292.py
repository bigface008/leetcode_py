# https://leetcode.cn/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/?envType=daily-question&envId=2026-01-19
from typing import List, Dict, Optional


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        M, N = len(mat), len(mat[0])
        pre_sum = [[0] * (N + 1) for _ in range(M + 1)]
        start, end = 0, min(M, N) + 1
        for i in range(M):
            for j in range(N):
                pre_sum[i + 1][j + 1] = pre_sum[i + 1][j] + pre_sum[i][j + 1] - pre_sum[i][j] + mat[i][j]
                if start == 0 and mat[i][j] <= threshold:
                    start = 1

        def check_valid(side: int) -> bool:
            for i in range(M - side + 1):
                for j in range(N - side + 1):
                    square_sum = pre_sum[i + side][j + side] - pre_sum[i + side][j] - pre_sum[i][j + side] + pre_sum[i][
                        j]
                    if square_sum <= threshold:
                        return True
            return False

        while start < end:
            mid = (start + end) // 2
            if check_valid(mid):
                start = mid + 1
            else:
                end = mid
        if not check_valid(start):
            start -= 1
        return start if 0 <= start <= min(M, N) else 0


if __name__ == '__main__':
    # print(
    #     Solution().maxSideLength([[2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2]], 1))
    # print(Solution().maxSideLength([[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]], 4))
    print(Solution().maxSideLength([[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]], 6))
