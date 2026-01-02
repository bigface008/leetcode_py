# https://leetcode.cn/problems/minimum-penalty-for-a-shop/?envType=daily-question&envId=2025-12-26
from typing import List, Dict, Tuple, Optional
from math import inf


# dfs(i) =
#   if customers[i] == 1:
#

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        open_cost = 0
        close_cost = sum(c == 'Y' for i, c in enumerate(customers))
        earliest_close_time = 0
        lowest_cost = close_cost
        for i, c in enumerate(customers):
            if c == 'Y':
                close_cost -= 1
            else:
                open_cost += 1
            cost = close_cost + open_cost
            if cost < lowest_cost:
                earliest_close_time = i + 1
                lowest_cost = cost
        return earliest_close_time


if __name__ == '__main__':
    print(Solution().bestClosingTime("YYNY"))

