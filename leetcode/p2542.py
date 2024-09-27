import heapq
from typing import List
from math import inf


# https://leetcode.com/problems/maximum-subsequence-score/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        new_arr = [(b, a) for a, b in zip(nums1, nums2)]
        new_arr.sort()
        N = len(new_arr)
        i = 0
        min_heap = []
        while i < k:
            heapq.heappush(min_heap, new_arr[N - 1 - i][1])
            i += 1
        sum_a = sum(min_heap)
        ans = sum_a * new_arr[N - k][0]
        while i < N:
            curr = new_arr[N - 1 - i][1]
            top = min_heap[0]
            if top < curr:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, new_arr[N - 1 - i][1])
                sum_a += curr - top
            ans = max(ans, sum_a * new_arr[N - 1 - i][0])
            i += 1
        return ans



def tst_group(nums: List[int], k: int):
    groups = []
    path = []

    def dfs(i: int):
        if len(path) == k:
            groups.append(path.copy())
            return
        if i == len(nums):
            return
        path.append(i)
        dfs(i + 1)
        path.pop()
        dfs(i + 1)

    dfs(0)
    print(groups)


if __name__ == '__main__':
    tst_group([0, 1, 2, 3, 4, 5, 6, 7], 3)
