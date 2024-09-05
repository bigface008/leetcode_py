from collections import defaultdict
from typing import List
from math import inf
import heapq


# https://leetcode.com/problems/path-with-maximum-probability/?envType=daily-question&envId=2024-08-27
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        graph = defaultdict(set)
        for i, e in enumerate(edges):
            u, v = e
            graph[u].add((v, succProb[i]))
            graph[v].add((u, succProb[i]))

        dist = [0.0] * n
        dist[start_node] = 1.0
        min_heap = [(-1.0, start_node)]
        while min_heap:
            prob, node = heapq.heappop(min_heap)
            prob = -prob
            for next_node, path_prob in graph[node]:
                p = path_prob * prob
                if p > dist[next_node]:
                    dist[next_node] = p
                    heapq.heappush(min_heap, (-p, next_node))
        return dist[end_node]







        # graph = defaultdict(set)
        # for i, e in enumerate(edges):
        #     u, v = e
        #     graph[u].add((v, succProb[i]))
        #     graph[v].add((u, succProb[i]))
        # dist = [0.0] * n
        # dist[start_node] = 1.0
        # min_heap = [(-1.0, start_node)] # (prob, node)
        # while min_heap:
        #     prob, node = heapq.heappop(min_heap)
        #     prob = -prob
        #     if prob < dist[node]:
        #         continue
        #     for next_node, edge_prob in graph[node]:
        #         p = edge_prob * prob
        #         if p > dist[next_node]:
        #             dist[next_node] = p
        #             heapq.heappush(min_heap, (-p, next_node))
        # return dist[end_node]


# class Solution:
#     def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
#                        end_node: int) -> float:
#         ans = float(0)
#         edges_mp = defaultdict(set) # node idx -> edges idx
#         for i, e in enumerate(edges):
#             n1, n2 = e
#             edges_mp[n1].add(i)
#             edges_mp[n2].add(i)
#         visited_edges = [False] * len(edges)
#         visited_points = [False] * n
#
#         def dfs(ni: int, curr_prod: float):
#             if ni == end_node:
#                 nonlocal ans
#                 ans = max(ans, curr_prod)
#                 return
#             curr_edges = edges_mp[ni]
#             visited_points[ni] = True
#             if not curr_edges:
#                 return
#             for ei in curr_edges:
#                 if visited_edges[ei]:
#                     continue
#                 n1, n2 = edges[ei]
#                 if n1 == ni:
#                     n1 = n2
#                 if visited_points[n1]:
#                     continue
#                 visited_edges[ei] = True
#                 dfs(n1, curr_prod * succProb[ei])
#                 visited_edges[ei] = False
#             visited_points[ni] = False
#
#         dfs(start_node, 1)
#         return ans

