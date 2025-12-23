# https://leetcode.cn/problems/number-of-ways-to-divide-a-long-corridor/?envType=daily-question&envId=2025-12-14
from typing import List


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = pow(10, 9) + 7
        chair_pos: List[int] = []
        chair_cnt = 0
        N = len(corridor)
        i = 0
        ans = 1
        while i < N:
            item = corridor[i]
            if item == 'S':
                chair_cnt += 1
                if len(chair_pos) == 2:
                    prev_chair = chair_pos[-1]
                    choice_cnt = i - prev_chair
                    ans *= choice_cnt
                    chair_pos = []
                chair_pos.append(i)
            i += 1
        if chair_cnt == 0 or chair_cnt % 2 == 1:
            return 0
        return ans % MOD


if __name__ == '__main__':
    print(Solution().numberOfWays('PPSPSP'))
    print(Solution().numberOfWays('SSPPSPS'))
