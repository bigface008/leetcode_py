# https://leetcode.com/problems/two-best-non-overlapping-events/?envType=daily-question&envId=2024-12-08
import bisect
import heapq
from typing import List
from functools import cache

import utils


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        N = len(events)
        events.sort()
        pq = []
        max_val = 0
        max_sum = 0
        for event in events:
            while pq and pq[0][0] < event[0]:
                max_val = max(max_val, pq[0][1])
                heapq.heappop(pq)
            max_sum = max(max_sum, max_val + event[2])
            heapq.heappush(pq, (event[1], event[2]))
        return max_sum


class Solution6:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        N = len(events)
        events.sort(key=lambda e: e[1])

        dp = [[0] * 3 for _ in range(N)]
        dp[0][1] = events[0][2]
        dp[0][2] = events[0][2]
        for i in range(1, N):
            curr = events[i]
            for remain in (1, 2):
                idx = bisect.bisect_left(range(0, i), True, key=lambda k: events[k][1] >= curr[0]) - 1
                res = max(curr[2], dp[i - 1][remain])
                if idx != i and idx >= 0:
                    res = max(res, curr[2] + dp[idx][remain - 1])
                dp[i][remain] = res
        return dp[N - 1][2]


class Solution5:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        N = len(events)
        events.sort(key=lambda e: e[1])

        @cache
        def dfs(i: int, remain: int) -> int:
            if remain == 0:
                return 0
            if i == 0:
                return events[0][2]
            curr = events[i]

            idx = bisect.bisect_left(range(0, i), True, key=lambda k: events[k][1] >= curr[0]) - 1
            res = max(curr[2], dfs(i - 1, remain))
            if idx != i and idx >= 0:
                res = max(res, curr[2] + dfs(idx, remain - 1))
            return res

        return dfs(N - 1, 2)


class Solution4:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        N = len(events)
        events.sort(key=lambda e: e[1])

        @cache
        def dfs(i: int, remain: int) -> int:
            if remain == 0:
                return 0
            if i == 0:
                return events[0][2]
            curr = events[i]
            idx = i
            for j in range(i - 1, -1, -1):
                prev = events[j]
                if prev[1] < curr[0]:
                    idx = j
                    break
            res = max(curr[2], dfs(i - 1, remain))
            if idx != i:
                res = max(res, curr[2] + dfs(idx, remain - 1))
            return res

        return dfs(N - 1, 2)


class Solution3:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        N = len(events)
        events.sort(key=lambda e: e[1])
        print('sorted', events)

        @cache
        def dfs(i: int) -> int:
            if i == 0:
                print(f'i={i} res={events[0][2]}')
                return events[0][2]
            curr = events[i]
            idx = i
            for j in range(i - 1, -1, -1):
                prev = events[j]
                if prev[1] < curr[0]:
                    idx = j
                    break
            res = max(curr[2], dfs(i - 1))
            if idx != i:
                res = max(res, curr[2] + dfs(idx))
            print(f'i={i} idx={idx} res={res}')
            return res

        return dfs(N - 1)


class Solution2:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        N = len(events)
        events.sort()
        end_range = [0] * N
        max_end = events[0][2]
        for i, event in enumerate(events):
            max_end = max(max_end, event[2])
            end_range[i] = max_end

        @cache
        def dfs(i: int) -> int:
            if i == 0:
                print(f'i={i} res={events[0][2]}')
                return events[0][2]
            curr = events[i]
            idx = i
            for j in range(i - 1, -1, -1):
                prev = events[j]
                if prev[1] < curr[0]:
                    idx = j
                    break
            res = max(curr[2], dfs(i - 1))
            if idx != i:
                res = max(res, curr[2] + dfs(idx))
            print(f'i={i} idx={idx} res={res}')
            return res

        return dfs(N - 1)


def check(events: List[List[int]], expect: int):
    temp = events.copy()
    output = Solution().maxTwoEvents(events)
    utils.tst(f'events={temp}', output, expect)


if __name__ == '__main__':
    check([[1, 3, 2], [4, 5, 2], [2, 4, 3]], 4)
    # check([[10, 83, 53], [63, 87, 45], [97, 100, 32], [51, 61, 16]], 85)
    # [[1, 3, 2], [4, 5, 2], [2, 4, 3]]
    # [[1, 3, 2], [2, 4, 3], [4, 5, 2]]
    # arr = [False, True, True]
    #
    # def check(k: int) -> bool:
    #     return arr[k]
    #
    # idx = bisect.bisect_left(range(0, 2), True, key=check) - 1
    # print(idx)