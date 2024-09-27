from typing import List

import utils


# https://leetcode.cn/problems/the-latest-time-to-catch-a-bus/?envType=daily-question&envId=2024-09-18
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        N = len(buses)
        M = len(passengers)
        buses.sort()
        passengers.sort()
        j = 0 # passenger idx
        for bus_time in buses:
            cnt = capacity
            while cnt and j < M and passengers[j] <= bus_time:
                cnt -= 1
                j += 1

        j -= 1
        ans = buses[-1] if cnt else passengers[j]
        while j >= 0 and passengers[j] == ans:
            ans -= 1
            j -= 1
        return ans



        # N = len(buses)
        # M = len(passengers)
        # buses.sort()
        # passengers.sort()
        # # i, j = 0, 0
        # info = []
        # j = 0
        # for i, bus in enumerate(buses):
        #     cnt = 0
        #     info.append([])
        #     while j < M and passengers[j] <= bus and cnt < capacity:
        #         cnt += 1
        #         info[-1].append(j)
        #         j += 1
        #
        # for i in range(len(info) - 1, -1, -1):
        #     group = info[i]
        #     NG = len(group)
        #     if not group:
        #         return buses[i]
        #     if NG < capacity:
        #         tmp = passengers[group[-1]]
        #         if tmp < buses[i]:
        #             return buses[i]
        #         # TODO: tmp == buses[i]?
        #     for j in range(NG - 1, -1, -1):
        #         idx = group[j]
        #         tmp = passengers[idx]
        #         if idx >= 0 and tmp - 1 != passengers[idx - 1]:
        #             return tmp - 1
        #         elif idx == 0 and tmp == buses[i]:
        #             return tmp - 1

        # for i in range(len(info) - 1, -1, -1):
        #     group = info[i]
        #     NG = len(group)
        #     if not group:
        #         return buses[i]
        #     if NG < capacity:
        #         tmp = passengers[group[-1]]
        #         if tmp < buses[i]:
        #             return buses[i]
        #         else:
        #             return tmp - 1
        #     for j in range(NG - 1, 0, -1):
        #         tmp = passengers[group[j]]
        #         if tmp - 1 != passengers[group[j - 1]]:
        #             return tmp - 1
        #     tmp = passengers[group[0]]
        #     return tmp - 1
        # return -1


def tst(buses: List[int], passengers: List[int], capacity: int, expect: int):
    output = Solution().latestTimeCatchTheBus(buses, passengers, capacity)
    utils.tst(f'buses={buses} passengers={passengers} capacity={capacity}', output, expect)


if __name__ == '__main__':
    tst([20, 30, 10], [19, 13, 26, 4, 25, 11, 21], 2, 20)
    tst([5], [2, 3], 10000, 5)
    tst([2, 3], [3, 2], 2, 1)
