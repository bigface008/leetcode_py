from functools import cache
from math import inf, log2, ceil

import utils


# https://leetcode.com/problems/race-car/
class Solution:
    def racecar(self, target: int) -> int:

        @cache
        def dfs(t: int) -> int:
            ans = inf
            forward = 1
            while (1 << forward) - 1 < 2 * t:
                forward_dist = (1 << forward) - 1
                if forward_dist == t:
                    return forward
                elif forward_dist > t:
                    ans = min(ans, forward + 1 + dfs(forward_dist - t))
                else:
                    for backward in range(forward):
                        backward_dist = (1 << backward) - 1
                        ans = min(ans, forward + 1 + backward + 1 + dfs(t - forward_dist + backward_dist))
                forward += 1
            return ans

        return dfs(target)


# wtf? https://leetcode.com/problems/race-car/solutions/2451845/python3-bfs-explanation
class Solution3:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 0, 1)])
        visited = set()
        while queue:
            moves, position, speed = queue.popleft()
            if position == target:
                return moves
            if (position, speed) in visited:
                continue
            else:
                visited.add((position, speed))
                queue.append((moves + 1, position + speed, speed * 2))
                if (position + speed > target and speed > 0) or (position + speed < target and speed < 0):
                    speed = -1 if speed > 0 else 1
                    queue.append((moves + 1, position, speed))
        return 0


# class Solution:
#     def racecar(self, target: int) -> int:
#
#         @cache
#         def dfs(t: int, speed: int, next_r: bool = False) -> int:
#             print(f'>> t={t} speed={speed}')
#             if t == 0:
#                 return 0 if speed == 1 else inf
#             if t == 1:
#                 if speed == 2:
#                     return 1
#                 elif speed == -1:
#                     return 2
#                 else:
#                     return inf
#             ans = 0
#             if speed >= 2:
#                 ans = dfs(t - speed // 2, speed // 2) + 1
#             elif speed == 1:
#                 max_speed = (t + 1)
#                 sp = 1 if not next_r else 2
#                 tmp = inf
#                 while sp < max_speed:
#                     tmp = min(tmp, dfs(t, -sp, True))
#                     sp *= 2
#                 ans = tmp + 1 # min(dfs(t, prev_speed)) + 'R'; prev_speed < 0 # 不确定的值，就意味着要取极值！
#             elif speed == -1:
#                 max_speed = (t + 1)
#                 sp = 1 if not next_r else 2
#                 tmp = inf
#                 while sp < max_speed:
#                     tmp = min(tmp, dfs(t, sp, True))
#                     sp *= 2
#                 ans = tmp + 1
#                 # min(dfs(t, prev_speed)) + 'R'; prev_speed > 0
#             elif speed < -1:
#                 ans = dfs(t - speed // 2, speed // 2) + 1
#             print(f'<< t={t} speed={speed} ans={ans}')
#             return ans
#         # abs speed [1, log2(target)]
#
#         ret = inf
#         sp = 1
#         max_speed = (target + 1)
#         while sp <= max_speed:
#             ret = min(ret, dfs(target, sp))
#             sp *= 2
#         ret += 1
#         return ret


def tst(target: int, expect: int):
    output = Solution().racecar(target)
    utils.tst(f'race target={target}', output, expect)


if __name__ == '__main__':
    tst(3, 2)
    tst(6, 5)
