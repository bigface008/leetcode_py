# https://leetcode.cn/problems/maximum-number-of-eaten-apples/?envType=daily-question&envId=2024-12-24
import heapq
from typing import List

import utils


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        N = len(apples)
        hp = []
        ans = 0
        i = 0
        while i < N or hp:
            if i < N:
                apple, day = apples[i], days[i]
                if apple:
                    heapq.heappush(hp, [i + day, apple])
            while hp and hp[0][0] <= i:
                heapq.heappop(hp)
            if hp:
                ans += 1
                hp[0][1] -= 1
                if hp[0][1] == 0:
                    heapq.heappop(hp)
            i += 1
        return ans


class Solution2:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        N = len(apples)
        hp = []
        ans = 0
        for i in range(N):
            apple, day = apples[i], days[i]
            if apple:
                heapq.heappush(hp, (i + day, apple))
            while hp and hp[0][0] <= i:
                heapq.heappop(hp)
            if hp:
                ans += 1
                td, ta = hp[0]
                if ta > 1:
                    heapq.heapreplace(hp, (td, ta - 1))
                else:
                    heapq.heappop(hp)
        i = N
        while hp:
            while hp and hp[0][0] <= i:
                heapq.heappop(hp)
            if not hp:
                break
            ans += 1
            i += 1
            td, ta = hp[0]
            if ta > 1:
                heapq.heapreplace(hp, (td, ta - 1))
            else:
                heapq.heappop(hp)
        return ans


def check(apples: List[int], days: List[int], ans: int) -> None:
    output = Solution().eatenApples(apples, days)
    utils.tst(f'apples={apples} days={days}', output, ans)


if __name__ == '__main__':
    check([1, 2, 3, 5, 2], [3, 2, 1, 4, 2], 7)
