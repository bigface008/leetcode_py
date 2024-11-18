from heapq import heapify
from typing import List
import heapq


def sol(arr1: List[int], arr2: List[int], K: int) -> int:
    M = len(arr1)
    N = len(arr2)
    ans = 0

    min_heap = []
    for x in arr1:
        if len(min_heap) < K:
            heapq.heappush(min_heap, x)

    for i, x in enumerate(arr2):
        top = arr1[0]
        if x > top:
            heapq.heappush(min_heap, x)
            heapq.heappop(min_heap)
        ans += top

    return ans