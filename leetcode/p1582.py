# https://leetcode.com/problems/special-positions-in-a-binary-matrix/?envType=daily-question&envId=2026-03-04
from typing import List, Dict, Tuple, Set, Optional


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        M, N = len(mat), len(mat[0])
        ans = 0
        for r, row in enumerate(mat):
            row_one_idx: Optional[int] = None
            valid = False
            for c, x in enumerate(row):
                if x == 1:
                    if row_one_idx is None:
                        valid = True
                        row_one_idx = c
                    else:
                        valid = False
                        break
            if not valid:
                continue
            for r2 in range(M):
                if mat[r2][row_one_idx] == 1 and r != r2:
                    valid = False
                    break
            if valid:
                ans += 1
        return ans




if __name__ == "__main__":
    print(Solution().numSpecial([[1,0,0],[0,0,1],[1,0,0]]))
