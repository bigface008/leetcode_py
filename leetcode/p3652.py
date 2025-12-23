# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/description/?envType=daily-question&envId=2025-12-18
from typing import List, Dict, Tuple, Optional


# i   i - k // 2   i - k

# k=4
# 0 1 2 3
# 0 0 1 1
# i=4
# 0 1 2 3 4
# x 0 0 1 1


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        N = len(prices)
        window_profit = 0
        for i in range(k // 2, k):
            window_profit += prices[i]
        for i in range(k, N):
            window_profit += strategy[i] * prices[i]
        ans = max(window_profit, sum(prices[i] * strategy[i] for i in range(N)))
        for i in range(k, N):
            window_profit = window_profit + prices[i] * (1 - strategy[i]) - prices[i - k // 2] + prices[i - k] * \
                            strategy[i - k]
            ans = max(ans, window_profit)
        return ans


if __name__ == '__main__':
    print(Solution().maxProfit([5, 4, 3], [1, 1, 0], 2))
