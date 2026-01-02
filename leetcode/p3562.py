# https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/?envType=daily-question&envId=2025-12-16
from collections import defaultdict
from typing import List, Dict, Optional, Tuple
from functools import cache, wraps
from math import inf


# dfs2(neighbors, rb, neighbor_parent_buy) -> int
#   v = neighbors[0]
#   for b in [1, rb]:
#     = max(future[v] - present[v] + dfs2(neighbors[1:], rb - present[v], nei...), dfs
#

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        graph: Dict[int, List[int]] = defaultdict(list)
        for u, v in hierarchy:
            graph[u - 1].append(v - 1)
        graph[-1].append(0) # 方便处理根节点所在层

        @cache
        def dfs(parent: int, level_start_idx: int, remain_budget: int, parent_buy: bool) -> int:
            if remain_budget < 0: # 负的budget不合法，返回-inf丢弃当前结果
                print(
                    f'parent={parent} level_start_idx={level_start_idx} remain_budget={remain_budget}, parent_buy={parent_buy} => res={-inf}')
                return -inf
            if remain_budget == 0: # 没有剩余budget直接返回0
                print(
                    f'parent={parent} level_start_idx={level_start_idx} remain_budget={remain_budget}, parent_buy={parent_buy} => res={0}')
                return 0
            level = graph[parent] # 当前层。
            N = len(level)
            if level_start_idx >= N: # 当前层的节点已遍历完
                print(
                    f'parent={parent} level_start_idx={level_start_idx} remain_budget={remain_budget}, parent_buy={parent_buy} => res={0}')
                return 0
            node = level[level_start_idx] # 当前节点
            cost = present[node] // 2 if parent_buy else present[node]
            node_profit = future[node] - cost
            res = max(0, node_profit) if remain_budget >= cost else 0
            if level_start_idx + 1 == N: # 当前处理的"森林"只剩下一棵树
                if remain_budget >= cost: # 剩余budget足够覆盖当前节点成本，考虑购买当前节点
                    res = max(res, node_profit + dfs(node, 0, remain_budget - cost, True))
                res = max(res, dfs(node, 0, remain_budget, False)) # 不购买当前节点
            else:
                if remain_budget >= cost:
                    # 枚举分配给当前节点子树的budget，计算"剩余budget足够覆盖当前节点成本"时，当前节点+当前节点子树+当前节点同层的总利润
                    for subtree_budget in range(0, remain_budget - cost + 1):
                        res = max(res, node_profit + dfs(node, 0, subtree_budget, True) + \
                                  dfs(parent, level_start_idx + 1, remain_budget - cost - subtree_budget, parent_buy))
                for subtree_budget in range(0, remain_budget + 1):
                    res = max(res, dfs(node, 0, subtree_budget, False) + \
                              dfs(parent, level_start_idx + 1, remain_budget - subtree_budget, parent_buy))
            print(f'parent={parent} level_start_idx={level_start_idx} remain_budget={remain_budget}, parent_buy={parent_buy} => res={res}')
            return res

        return dfs(-1, 0, budget, False)


# dfs(v, rb, v_parent_buy)
# if v_parent_buy:
#   = max(future[v] - present[v] // 2 + dfs2(ui, rb - present[v] // 2, true)), ...
# else:
#   = max(future[v] - present[v] + dfs(ui, rb - present[v], true)) ...

# 注意这个解法是错的，但是目前不清楚哪里错了。


# class Solution:
#     def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
#         graph: List[List[int]] = [[] for _ in range(n)]
#         for u, v in hierarchy:
#             graph[u - 1].append(v - 1)
#
#         @cache
#         def dfs(parent: int, neighbor_start_idx: int, remain_budget: int, parent_buy: bool) -> int:
#             if remain_budget <= 0:
#                 return 0
#             if parent == -1:
#                 neighbors = (0,)
#             else:
#                 neighbors = graph[parent]
#                 if len(neighbors) == 0 or neighbor_start_idx >= len(neighbors):
#                     return 0
#             v = neighbors[neighbor_start_idx]
#             price = (present[v] // 2) if parent_buy else present[v]
#             profit = future[v] - price
#             res = max(profit, 0) if price <= remain_budget else 0
#             if neighbor_start_idx + 1 == len(neighbors):
#                 res = max(res, dfs(v, 0, remain_budget, False))
#                 if remain_budget - price >= 0:
#                     res = max(res, profit + dfs(v, 0, remain_budget - price, True))
#                 return res
#             else:
#                 for sub_tree_budget in range(0, remain_budget - price + 1):
#                     res = max(res, profit + dfs(v, 0, sub_tree_budget, True) + dfs(parent, neighbor_start_idx + 1,
#                                                                                    remain_budget - sub_tree_budget - price,
#                                                                                    parent_buy))
#                 for sub_tree_budget in range(0, remain_budget + 1):
#                     res = max(res, dfs(v, 0, sub_tree_budget, False) + dfs(parent, neighbor_start_idx + 1,
#                                                                            remain_budget - sub_tree_budget,
#                                                                            parent_buy))
#                 return res
#
#         return dfs(-1, 0, budget, False)


if __name__ == '_main__':
    # print(Solution().maxProfit(3, [4, 6, 8], [7, 9, 11], [[1, 2], [1, 3]], 10))
    # print(Solution().maxProfit(2, [1, 2], [4, 3], [[1, 2]], 3))
    print(Solution().maxProfit(29,
                               [20, 8, 26, 3, 9, 24, 20, 5, 11, 15, 11, 29, 9, 18, 17, 49, 46, 9, 48, 1, 50, 6, 30, 39,
                                26, 14, 33, 26, 45],
                               [28, 43, 34, 41, 45, 36, 33, 10, 17, 22, 25, 18, 33, 5, 13, 6, 11, 50, 40, 32, 24, 10,
                                46, 30, 43, 16, 34, 37, 35],
                               [[1, 3], [1, 24], [3, 22], [1, 14], [3, 26], [22, 21], [14, 12], [26, 11], [21, 18],
                                [26, 8], [26, 27], [26, 6], [27, 23], [8, 13], [13, 19], [21, 10], [24, 2], [13, 4],
                                [6, 17], [23, 29], [12, 25], [11, 20], [27, 5], [20, 7], [10, 15], [17, 9], [10, 16],
                                [15, 28]], 119))
    # print(Solution().maxProfit(2, [3, 4], [5, 8], [[1, 2]], 4))
