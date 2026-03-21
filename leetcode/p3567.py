# https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/?envType=daily-question&envId=2026-03-20
from collections import defaultdict

from sortedcontainers import SortedDict
from typing import List, Dict, Set
from itertools import pairwise
from math import inf


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        M, N = len(grid), len(grid[0])
        ans = [[0] * (N - k + 1) for _ in range(M - k + 1)]
        for i in range(M - k + 1):
            for j in range(N - k + 1):
                st: Set[int] = set()
                for r in range(k):
                    for c in range(k):
                        st.add(grid[i + r][j + c])
                if len(st) == 1:
                    continue
                ks = list(st)
                ks.sort()
                ans[i][j] = min(k2 - k1 for k1, k2 in pairwise(ks))
        return ans


        # freq_mp: Dict[int, int] = SortedDict()
        # for i in range(k):
        #     for j in range(k):
        #         freq_mp[grid[i][j]] += 1
        # ans = [[0] * (N - k + 1) for _ in range(M - k + 1)]
        # ans[0][0] = min(k2 - k1 for k1, k2 in pairwise(freq_mp.keys()))
        # for i in range(M - k + 1):
        #     for j in range(N - k + 1):
        #         pass


if __name__ == "__main__":
    print(Solution().minAbsDiff([[3,-1]], 1))
