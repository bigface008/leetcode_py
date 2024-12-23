# https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/
import heapq
from collections import defaultdict
from typing import List
from math import inf


class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        graph = defaultdict(set)
        N = 0
        for u, v, t in edges:
            graph[u].add((v, t))
            graph[v].add((u, t))
            N = max(N, u + 1, v + 1)
        fees = [[inf] * (maxTime + 1) for _ in range(N)]
        pq = [(passingFees[0], 0, 0)]  # fee, i, time
        while pq:
            fee, i, time = pq[0]
            heapq.heappop(pq)
            for n, t in graph[i]:
                new_fee = fee + passingFees[n]
                new_time = t + time
                if new_time <= maxTime and fees[n][new_time] > new_fee:
                    fees[n][new_time] = new_fee
                    heapq.heappush(pq, (new_fee, n, new_time))
        res = min(fees[-1])
        return res if res is not inf else -1

        # graph = defaultdict(set)
        # N = 0
        # for u, v, t in edges:
        #     graph[u].add((v, t))
        #     graph[v].add((u, t))
        #     N = max(N, u + 1, v + 1)
        # times = [inf] * N
        # times[0] = 0
        # pq = [(passingFees[0], 0, 0)] # fee, i, time
        # while pq:
        #     fee, i, time = pq[0]
        #     if i == N - 1:
        #         return fee
        #     heapq.heappop(pq)
        #     for n, t in graph[i]:
        #         new_fee = fee + passingFees[n]
        #         new_time = t + time
        #         if times[n] > new_time and new_time <= maxTime:
        #             times[n] = new_time
        #             heapq.heappush(pq, (new_fee, n, new_time))
        # return -1
