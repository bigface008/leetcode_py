# 两个数组中各取两个元素，返回乘积最小的前k个组合
import heapq
from heapq import heapify
from typing import Tuple, List


def solution(arr1: List[int], arr2: List[int], k: int) -> List[Tuple[int, int]]:
    N1, N2 = len(arr1), len(arr2)
    hp = []
    max_in_hp = 0
    for i in range(N1):
        for j in range(N2):
            prod = arr1[i] * arr2[j]
            if len(hp) >= k and max_in_hp < prod:
                break
            hp.append((prod, i, j))
    heapq.heapify(hp)

    ans = []
    cnt = 0
    while cnt < k:
        prod, i, j = hp.pop()
        ans.append((i, j))
        cnt += 1
    return ans
