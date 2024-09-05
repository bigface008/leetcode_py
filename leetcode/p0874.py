from collections import defaultdict
from typing import List

import utils


# https://leetcode.com/problems/walking-robot-simulation/?envType=daily-question&envId=2024-09-04
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs_mp = defaultdict(set)
        for x, y in obstacles:
            obs_mp[x].add(y)

        direction = 0  # 0: up 1: right: 2:down 3:left
        x, y = 0, 0
        ans = 0
        for cmd in commands:
            print(f'cmd={cmd} x={x} y={y} direction={direction}')
            if cmd > 0:
                for i in range(cmd):
                    nx, ny = x, y
                    if direction == 0:
                        ny += 1
                    elif direction == 1:
                        nx += 1
                    elif direction == 2:
                        ny -= 1
                    else:
                        nx -= 1
                    if ny in obs_mp[nx]:
                        break
                    x, y = nx, ny
                    ans = max(ans, pow(nx, 2) + pow(ny, 2))
                print(f'  arrive at x={x} y={y}')
            elif cmd == -1:
                direction = (direction + 1) % 4
            else:
                direction = (direction + 3) % 4
        return ans


def tst(commands: List[int], obstacles: List[List[int]], expect: int):
    output = Solution().robotSim(commands, obstacles)
    utils.tst(f'commands={commands} obstacles={obstacles}', output, expect)


if __name__ == '__main__':
    # tst([4, -1, 3], [], 25)
    tst([4, -1, 4, -2, 4], [[2, 4]], 65)
    # tst([6, -1, -1, 6], [], 36)
