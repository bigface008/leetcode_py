# https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/?envType=daily-question&envId=2025-12-16
from typing import List, Dict, Optional, Tuple
from functools import cache, wraps


# dfs2(neighbors, rb, neighbor_parent_buy) -> int
#   v = neighbors[0]
#   for b in [1, rb]:
#     = max(future[v] - present[v] + dfs2(neighbors[1:], rb - present[v], nei...), dfs
#

# dfs(v, rb, v_parent_buy)
# if v_parent_buy:
#   = max(future[v] - present[v] // 2 + dfs2(ui, rb - present[v] // 2, true)), ...
# else:
#   = max(future[v] - present[v] + dfs(ui, rb - present[v], true)) ...

# 注意这个解法是错的，但是目前不清楚哪里错了。


class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        graph: List[List[int]] = [[] for _ in range(n)]
        for u, v in hierarchy:
            graph[u - 1].append(v - 1)

        @cache
        def dfs(parent: int, neighbor_start_idx: int, remain_budget: int, parent_buy: bool) -> int:
            if remain_budget <= 0:
                return 0
            if parent == -1:
                neighbors = (0,)
            else:
                neighbors = graph[parent]
                if len(neighbors) == 0 or neighbor_start_idx >= len(neighbors):
                    return 0
            v = neighbors[neighbor_start_idx]
            price = (present[v] // 2) if parent_buy else present[v]
            profit = future[v] - price
            res = max(profit, 0) if price <= remain_budget else 0
            if neighbor_start_idx + 1 == len(neighbors):
                res = max(res, dfs(v, 0, remain_budget, False))
                if remain_budget - price >= 0:
                    res = max(res, profit + dfs(v, 0, remain_budget - price, True))
                return res
            else:
                for sub_tree_budget in range(0, remain_budget - price + 1):
                    res = max(res, profit + dfs(v, 0, sub_tree_budget, True) + dfs(parent, neighbor_start_idx + 1,
                                                                                   remain_budget - sub_tree_budget - price,
                                                                                   parent_buy))
                for sub_tree_budget in range(0, remain_budget + 1):
                    res = max(res, dfs(v, 0, sub_tree_budget, False) + dfs(parent, neighbor_start_idx + 1,
                                                                           remain_budget - sub_tree_budget,
                                                                           parent_buy))
                return res

        return dfs(-1, 0, budget, False)


if __name__ == '__main__':
    # print(Solution().maxProfit(3, [4, 6, 8], [7, 9, 11], [[1, 2], [1, 3]], 10))
    print(Solution().maxProfit(2, [3, 4], [5, 8], [[1, 2]], 4))
