import collections
from typing import List


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        N = len(favorite)
        in_degree = [0] * N
        for i, f in enumerate(favorite):
            in_degree[f] += 1

        reverse_graph = [[] for _ in range(N)]

        # topo sort
        dq = collections.deque(i for i, d in enumerate(in_degree) if d == 0)
        while dq:
            x = dq.popleft()
            y = favorite[x]
            reverse_graph[y].append(x)
            in_degree[y] -= 1
            if in_degree[y] == 0:
                dq.append(y)

        def dfs(i: int) -> int:
            max_depth = 1
            for x in reverse_graph[i]:
                max_depth = max(max_depth, dfs(x) + 1)
            return max_depth

        max_ring_size, sum_chain_size = 0, 0
        for i, d in enumerate(in_degree):
            if d == 0:
                continue

            in_degree[i] = 0
            ring_size = 1
            x = favorite[i]
            while x != i:
                in_degree[x] = 0
                ring_size += 1
                x = favorite[x]

            if ring_size == 2:
                sum_chain_size += dfs(i) + dfs(favorite[i])
            else:
                max_ring_size = max(max_ring_size, ring_size)

        return max(max_ring_size, sum_chain_size)
