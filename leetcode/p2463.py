from typing import List

from more_itertools.recipes import factor
from sympy import limit

import utils
from math import inf
from functools import cache


# https://leetcode.com/problems/minimum-total-distance-traveled/?envType=daily-question&envId=2024-10-31
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        factory.sort()
        robot.sort()
        N = len(factory)
        M = len(robot)

        dp = [inf] * (M + 1)
        dp[0] = 0
        for pos, limit in factory:
            for robo_cnt in range(M, 0, -1):
                cost = 0
                for fix_robo_cnt in range(1, min(limit, robo_cnt) + 1):
                    cost += abs(robot[robo_cnt - fix_robo_cnt] - pos)
                    dp[robo_cnt] = min(dp[robo_cnt], dp[robo_cnt - fix_robo_cnt] + cost)
        return dp[-1]


# class Solution:
#     def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
#         factory.sort()
#         robot.sort()
#         N = len(factory)
#         M = len(robot)
#
#         dp = [[inf] * (M + 1) for _ in range(N + 1)]
#         for fact_cnt in range(N + 1):
#             dp[fact_cnt][0] = 0
#         for robo_cnt in range(M + 1):
#             if robo_cnt <= factory[0][1]:
#                 dp[1][robo_cnt] = sum(abs(factory[0][0] - robot[i]) for i in range(robo_cnt))
#         for fact_cnt in range(N + 1):
#             pos, limit = factory[fact_cnt - 1]
#             for robo_cnt in range(M + 1):
#                 res = dp[fact_cnt - 1][robo_cnt]
#                 fix_robo_cnt = 1
#                 dist_sum = 0
#                 while fix_robo_cnt <= min(robo_cnt, limit):
#                     dist_sum += abs(pos - robot[robo_cnt - fix_robo_cnt])
#                     res = min(res, dist_sum + dp[fact_cnt - 1][robo_cnt - fix_robo_cnt])
#                     fix_robo_cnt += 1
#                 dp[fact_cnt][robo_cnt] = res
#         return dp[N][M]


class Solution3:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        factory.sort()
        robot.sort()
        N = len(factory)
        M = len(robot)

        # i - factories; j - robots
        @cache
        def dfs(fact_cnt: int, robo_cnt: int) -> int:
            if robo_cnt == 0:
                return 0
            pos, limit = factory[fact_cnt - 1]
            if fact_cnt == 1:
                if robo_cnt > limit:
                    return inf
                else:
                    return sum(abs(pos - robot[i]) for i in range(robo_cnt))
            res = dfs(fact_cnt - 1, robo_cnt)
            fix_robo_cnt = 1
            dist_sum = 0
            while fix_robo_cnt <= min(robo_cnt, limit):
                dist_sum += abs(pos - robot[robo_cnt - fix_robo_cnt])
                res = min(res, dist_sum + dfs(fact_cnt - 1, robo_cnt - fix_robo_cnt))
                fix_robo_cnt += 1
            return res

        return dfs(N, M)


class Solution2:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        factory.sort()
        robot.sort()
        N = len(factory)
        M = len(robot)

        # i - factories; j - robots
        @cache
        def dfs(i: int, j: int) -> int:
            if j == M:
                return 0
            if i == N - 1:
                if factory[i][1] < M - j:
                    return inf
                else:
                    return sum(abs(factory[i][0] - x) for x in robot[j:])
            res = dfs(i + 1, j)
            dist_sum, robo_cnt = 0, 1
            while robo_cnt <= factory[i][1] and robo_cnt + j - 1 < M:
                dist_sum += abs(robot[robo_cnt + j - 1] - factory[i][0])
                res = min(res, dist_sum + dfs(i + 1, robo_cnt + j))
                robo_cnt += 1
            return res

        return dfs(0, 0)



def tst(robot: List[int], factory: List[List[int]], expect: int):
    output = Solution().minimumTotalDistance(robot, factory)
    utils.tst(f'min total dist robot={robot} factory={factory}', output, expect)


if __name__ == '__main__':
    tst([0, 4, 6], [[2, 2], [6, 2]])
