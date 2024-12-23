# https://leetcode.com/problems/redundant-connection/
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = 0
        for u, v in edges:
            N = max(u, v, N)

        ranks = [0] * N
        parents = [i for i in range(N)]

        def findParent(u: int) -> int:
            while parents[u] != u:
                parents[u] = parents[parents[u]]
                u = parents[u]
            return u

        for edge in edges:
            u, v = edge[0] - 1, edge[1] - 1
            pu = findParent(u)
            pv = findParent(v)
            if pv == pu:
                return edge
            if ranks[pu] > ranks[pv]:
                parents[pv] = pu
            elif ranks[pu] < ranks[pv]:
                parents[pu] = pv
            else:
                parents[pv] = pu
                ranks[pu] += 1
        return []