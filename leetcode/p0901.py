# https://leetcode.cn/problems/online-stock-span/
class StockSpanner:

    def __init__(self):
        self.prices = []
        self.max_stk = []

    def next(self, price: int) -> int:
        while self.max_stk and self.prices[self.max_stk[-1]] <= price:
            self.max_stk.pop()
        ans = len(self.prices) + 1
        if self.max_stk:
            ans = len(self.prices) - self.max_stk[-1]
        self.max_stk.append(len(self.prices))
        self.prices.append(price)
        return ans
