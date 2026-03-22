# https://leetcode.cn/problems/determine-whether-matrix-can-be-obtained-by-rotation/?envType=daily-question&envId=2026-03-22
from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        N = len(mat)
        if N % 2 == 1 and mat[N // 2][N // 2] != target[N // 2][N // 2]:
            return False
        is_0_valid, is_1_valid, is_2_valid, is_3_valid = True, True, True, True
        for i in range(N):
            for j in range(N):
                x = mat[i][j]
                a = target[i][j]
                b = target[j][N - 1 - i]
                c = target[N - 1 - i][N - 1 - j]
                d = target[N - 1 - j][i]
                if x != a:
                    is_0_valid = False
                if x != b:
                    is_1_valid = False
                if x != c:
                    is_2_valid = False
                if x != d:
                    is_3_valid = False
                if not (is_0_valid or is_1_valid or is_2_valid or is_3_valid):
                    return False
        return True


if __name__ == "__main__":
    # print(Solution().findRotation([[0, 0], [1, 1]], [[0, 1], [1, 0]]))
    print(Solution().findRotation([[0, 1], [1, 1]], [[1, 0], [0, 1]]))
