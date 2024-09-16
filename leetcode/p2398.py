from typing import List

import utils


# https://leetcode.com/problems/maximum-number-of-robots-within-budget/
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        N = len(chargeTimes)
        time_stk = []
        run_cost_sum = 0
        window_size = 0
        ans = 0
        left = 0
        for right in range(N):
            time = chargeTimes[right]
            window_size += 1
            run_cost_sum += runningCosts[right]
            while time_stk and chargeTimes[time_stk[-1]] <= time:
                time_stk.pop()
            time_stk.append(right)
            while window_size > 0 and time_stk and run_cost_sum * window_size + chargeTimes[time_stk[0]] > budget:
                if time_stk[0] == left:
                    time_stk.pop(0)
                run_cost_sum -= runningCosts[left]
                window_size -= 1
                left += 1
            ans = max(ans, window_size)
        return ans


def tst(chargeTimes: List[int], runningCosts: List[int], budget: int, expect: int):
    output = Solution().maximumRobots(chargeTimes, runningCosts, budget)
    utils.tst(f'chargeTimes={chargeTimes} runningCosts={runningCosts} budget={budget}', output, expect)


if __name__ == '__main__':
    tst([11, 12, 19], [10, 8, 7], 19, 0)
