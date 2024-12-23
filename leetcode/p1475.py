# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/?envType=daily-question&envId=2024-12-18
from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        N = len(prices)
        min_stk = []
        ans = prices.copy()
        for i in range(N - 1, -1, -1):
            p = prices[i]
            # while max_stk and prices[max_stk[-1]] <= p:
            #     max_stk.pop()
            # if max_stk:
            #     ans[i] -= prices[max_stk[-1]]
            # max_stk.append(i)
            while min_stk and prices[min_stk[-1]] >= p:
                min_stk.pop()
            if min_stk:
                ans[i] -= prices[min_stk[-1]]
            min_stk.append(i)
        return ans