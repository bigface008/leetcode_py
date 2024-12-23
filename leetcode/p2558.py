# https://leetcode.com/problems/take-gifts-from-the-richest-pile/?envType=daily-question&envId=2024-12-12
import heapq
import math
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        N = len(gifts)
        pq = [-x for x in gifts]
        heapq.heapify(pq)
        for _ in range(k):
            top = -pq[0]
            heapq.heappop(pq)
            heapq.heappush(pq, -math.floor(math.sqrt(top)))
        return -sum(pq)