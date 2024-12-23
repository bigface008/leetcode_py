# https://leetcode.cn/problems/closest-room/?envType=daily-question&envId=2024-12-16
import bisect
from typing import List
from math import inf
from sortedcontainers import SortedList

import utils


class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        N = len(rooms)
        Q = len(queries)
        rooms.sort(key=lambda r: r[1])

        ans = [-1] * Q
        j = N - 1
        room_ids = SortedList()
        for i in sorted(range(Q), key=lambda i: -queries[i][1]):
            prefer, min_size = queries[i]
            while j >= 0 and rooms[j][1] >= min_size:
                room_ids.add(rooms[j][0])
                j -= 1

            diff = inf
            k = room_ids.bisect_left(prefer)
            if k:
                diff = prefer - room_ids[k - 1]
                ans[i] = room_ids[k - 1]
            if k < len(room_ids) and room_ids[k] - prefer < diff:
                ans[i] = room_ids[k]
        return ans


        # N = len(rooms)
        # Q = len(queries)
        # rooms.sort(key=lambda room: (room[1], room[0]))
        # ans = [0] * Q
        # for qi, (prefer, min_size) in enumerate(queries):
        #     res = 0
        #     i1 = bisect.bisect_left(range(0, N), True, key=lambda i: rooms[i][1] >= min_size)
        #     if i1 == N:
        #         res = -1
        #     else:
        #         min_diff = inf
        #         res = -1
        #         for i2 in range(i1, N):
        #             diff = abs(prefer - rooms[i2][0])
        #             if min_diff > diff:
        #                 res = rooms[i2][0]
        #                 min_diff = diff
        #     ans[qi] = res
        # return ans


def check(rooms: List[List[int]], queries: List[List[int]], expect: List[int]):
    utils.tst(f'rooms={rooms.copy()} queries={queries}', Solution().closestRoom(rooms.copy(), queries), expect)


if __name__ == '__main__':
    # check([[1, 4], [2, 3], [3, 5], [4, 1], [5, 2]], [[2, 3], [2, 4], [2, 5]], [2, 1, 3])
    check([[23, 22], [6, 20], [15, 6], [22, 19], [2, 10], [21, 4], [10, 18], [16, 1], [12, 7], [5, 22]],
          [[12, 5], [15, 15], [21, 6], [15, 1], [23, 4], [15, 11], [1, 24], [3, 19], [25, 8], [18, 6]],
          [12, 10, 22, 15, 23, 10, -1, 5, 23, 15])
