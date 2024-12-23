# https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/?envType=daily-question&envId=2024-12-22
import heapq
from collections import defaultdict
from typing import List

import utils


class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        N, Q = len(heights), len(queries)
        ans = [-1] * Q
        qmp = defaultdict(list)
        for i, (a, b) in enumerate(queries):
            if a > b:
                a, b = b, a
            if a == b or heights[a] < heights[b]:
                ans[i] = b
            else:
                qmp[b].append((heights[a], i))

        min_hp = []
        for i, h in enumerate(heights):
            while min_hp and min_hp[0][0] < h:
                ans[heapq.heappop(min_hp)[1]] = i
            for q in qmp[i]:
                heapq.heappush(min_hp, q)
        return ans


class Solution2:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        N = len(heights)
        Q = len(queries)
        min_idx = N - 1
        q_set = defaultdict(list)
        for a, b in queries:
            min_idx = min(min_idx, a, b)
            q_set[a].clear()
            q_set[b].clear()

        max_stk = []
        for i in range(N - 1, -1, -1):
            h = heights[i]
            while max_stk and heights[max_stk[-1]] <= h:
                max_stk.pop()
            if i in q_set:
                q_set[i] = max_stk.copy()
            max_stk.append(i)

        ans = [-1] * Q
        for i, (a, b) in enumerate(queries):
            res = -1
            a_arr = q_set[a]
            b_arr = q_set[b]
            j1, j2 = len(a_arr) - 1, len(b_arr) - 1
            while j1 >= 0 and j2 >= 0:
                if a_arr[j1] == b_arr[j2]:
                    res = a_arr[j1]
                    break
                elif a_arr[j1] < b_arr[j2]:
                    j1 -= 1
                else:
                    j2 -= 1
            ans[i] = res
        return ans


def check(heights: List[int], queries: List[List[int]], expect: List[int]):
    output = Solution().leftmostBuildingQueries(heights, queries)
    utils.tst(f'leftmostBuildingQueries({heights}, {queries})', output, expect)


if __name__ == '__main__':
    check([6, 4, 8, 5, 2, 7], [[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]], [2, 5, -1, 5, 2])
