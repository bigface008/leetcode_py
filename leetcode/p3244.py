# https://leetcode.cn/problems/shortest-distance-after-road-addition-queries-ii/?envType=daily-question&envId=2024-11-20
from typing import List


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        Q = len(queries)
        ans = [0] * Q
        pa = list(range(n - 1))
        min_dist = n - 1

        def findParent(u: int) -> int:
            while pa[u] != u:
                pa[u] = pa[pa[u]]
                u = pa[u]
            return u

        for qi, (u, v) in enumerate(queries):
            pv = findParent(v - 1)
            i = findParent(u)
            while i < v - 1:
                min_dist -= 1
                pa[i] = pv
                i = findParent(i + 1)
            ans[qi] = min_dist
        return ans