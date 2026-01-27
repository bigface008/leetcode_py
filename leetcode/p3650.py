# https://leetcode.cn/problems/minimum-cost-path-with-edge-reversals/?envType=daily-question&envId=2026-01-27
import heapq
from typing import List
from math import inf


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        out_graph = [[] for _ in range(n)]
        in_graph = [[] for _ in range(n)]
        for u, v, w in edges:
            out_graph[u].append((v, w))
            in_graph[v].append((u, w))
        min_dist = [inf] * n
        pq = [(0, 0, -1)] # dist, idx, parent idx
        while pq:
            dist, node, node_parent = pq[0]
            heapq.heappop(pq)
            if dist > min_dist[node]:
                continue
            for out_neighbor, w in out_graph[node]:
                if out_neighbor == node_parent:
                    continue
                new_out_neighbor_dist = dist + w
                if new_out_neighbor_dist < min_dist[out_neighbor]:
                    min_dist[out_neighbor] = new_out_neighbor_dist
                    heapq.heappush(pq, (new_out_neighbor_dist, out_neighbor, node))
            for in_neighbor, w in in_graph[node]:
                if in_neighbor == node_parent:
                    continue
                new_in_out_neighbor_dist = dist + 2 * w
                if new_in_out_neighbor_dist < min_dist[in_neighbor]:
                    min_dist[in_neighbor] = new_in_out_neighbor_dist
                    heapq.heappush(pq, (new_in_out_neighbor_dist, in_neighbor, node))
        return min_dist[-1] if min_dist[-1] is not inf else -1


