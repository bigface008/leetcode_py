# https://leetcode.cn/problems/minimum-operations-to-equalize-binary-string/?envType=daily-question&envId=2026-02-27
from typing import List, Dict, Tuple
from sortedcontainers import SortedList


class Solution:
    def minOperations(self, s: str, k: int) -> int:
        N = len(s)
        not_visited = [SortedList(range(0, N + 1, 2)), SortedList(range(1, N + 1, 2))]
        not_visited[0].add(N + 1)
        not_visited[1].add(N + 1)

        start = s.count('0')
        not_visited[start % 2].discard(start)
        q = [start]
        ans = 0
        while q:
            tmp = q
            q = []
            for z in tmp:
                if z == 0:
                    return ans
                mn = z + k - 2 * min(k, z)
                mx = z + k - 2 * max(0, k - N + z)
                sl = not_visited[mn % 2]
                idx = sl.bisect_left(mn)
                while sl[idx] <= mx:
                    j = sl.pop(idx)
                    q.append(j)
            ans += 1
        return -1