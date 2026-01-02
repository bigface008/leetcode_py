# https://leetcode.cn/problems/last-day-where-you-can-still-cross/?envType=daily-question&envId=2025-12-31
from typing import List, Dict, Tuple, Optional


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))
        ALL = row * col + 2
        N = len(cells)
        parent: List[int] = list(range(ALL))
        score: List[int] = [0] * ALL
        is_land = [False] * ALL

        def find_parent(node: int) -> int:
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def connect(u: int, v: int):
            pu, pv = find_parent(u), find_parent(v)
            if score[pu] > score[pv]:
                parent[pv] = pu
            elif score[pu] < score[pv]:
                parent[pu] = pv
            else:
                parent[pv] = pu
                score[pu] += 1


        for day in range(N - 1, -1, -1):
            r, c = cells[day]
            r -= 1
            c -= 1
            u = r * col + c
            is_land[u] = True
            if r == row - 1:
                connect(u, ALL - 1)
            if r == 0:
                connect(u, ALL - 2)
            for dx, dy in DIR:
                x, y = r + dx, c + dy
                v = x * col + y
                if 0 <= x < row and 0 <= y < col and is_land[v]:
                    connect(u, v)
            if find_parent(ALL - 1) == find_parent(ALL - 2):
                return day
        return 0



        # DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))
        # point_to_date: Dict[int, int] = dict()
        # for i, (r, c) in enumerate(cells):
        #     point_to_date[(r - 1) * col + c - 1] = i + 1
        #
        # def is_valid(day: int) -> bool:
        #     if day <= 0:
        #         return True
        #     ALL = row * col + 2
        #     parent: List[int] = list(range(ALL))
        #     score: List[int] = [0] * ALL
        #
        #     def find_parent(node: int) -> int:
        #         while parent[node] != node:
        #             parent[node] = parent[parent[node]]
        #             node = parent[node]
        #         return node
        #
        #     def connect(u: int, v: int):
        #         pu, pv = find_parent(u), find_parent(v)
        #         if score[pu] > score[pv]:
        #             parent[pv] = pu
        #         elif score[pu] < score[pv]:
        #             parent[pu] = pv
        #         else:
        #             parent[pv] = pu
        #             score[pu] += 1
        #
        #     for r in range(row):
        #         for c in range(col):
        #             u = r * col + c
        #             if point_to_date[u] <= day:
        #                 continue
        #             if r == row - 1:
        #                 connect(u, ALL - 1)
        #             if r == 0:
        #                 connect(u, ALL - 2)
        #             for dx, dy in DIR:
        #                 x, y = r + dx, c + dy
        #                 v = x * col + y
        #                 if 0 <= x < row and 0 <= y < col and point_to_date[v] > day:
        #                     connect(u, v)
        #
        #     return find_parent(ALL - 1) == find_parent(ALL - 2)
        #
        # N = len(cells)
        # start, end = 0, N + 1
        # while start < end:
        #     mid = (start + end) // 2
        #     if is_valid(mid):
        #         start = mid + 1
        #     else:
        #         end = mid
        # if not is_valid(start):
        #     start -= 1
        # return start


if __name__ == '__main__':
    # print(Solution().latestDayToCross(2, 2, [[1, 1], [1, 2], [2, 1], [2, 2]]))
    # print(Solution().latestDayToCross(2, 2, [[1, 1], [2, 1], [1, 2], [2, 2]]))
    print(Solution().latestDayToCross(6, 2,
                                      [[4, 2], [6, 2], [2, 1], [4, 1], [6, 1], [3, 1], [2, 2], [3, 2], [1, 1], [5, 1],
                                       [5, 2], [1, 2]]))
