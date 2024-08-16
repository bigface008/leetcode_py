# 有互斥条件的背包问题。
# 在N个物品中，选取一部分放入最大承重为W的背包中，求其价值的和的最大值。
# 你tm竟然忘记背包咋做了......程序员之耻......
# 总之是一个二维的dp[i][j]，i表示从0到i的物品中选取，j表示物品限重
# https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E8%83%8C%E5%8C%85%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%8001%E8%83%8C%E5%8C%85-1.md
from collections import defaultdict
from typing import List, Tuple, Dict, Set


# details 是一个元组的数组，每个元组第一项是物品重量，第二项是物品价值
# conflict 表示和一个物品冲突的物品的集合。
def solution(capacity: int, details: List[Tuple[int, int]], conflicts: List[Tuple[int, int]]) -> int:
    n = len(details)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    item_included = [[False] * (capacity + 1) for _ in range(n + 1)]
    weights = [d[1] for d in details]
    values = [d[0] for d in details]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # If the item is not included
            dp[i][w] = dp[i - 1][w]

            # If the item is included
            if w >= weights[i - 1]:
                can_include = True
                for conflict_item in conflicts[i - 1]:
                    if item_included[i - 1][w - weights[i - 1]]:
                        can_include = False
                        break
                if can_include and dp[i][w] < dp[i - 1][w - weights[i - 1]] + values[i - 1]:
                    dp[i][w] = dp[i - 1][w - weights[i - 1]] + values[i - 1]
                    item_included[i][w] = True

    return dp[n][capacity]


# 普通背包问题
def normal_bag(W: int, details: List[Tuple[int, int]]) -> int:
    N = len(details)
    dp = [[0 for _ in range(W + 1)] for _ in range(N)]
    for j in range(W + 1):
        value, weight = details[0]
        if weight <= j:
            dp[0][j] = value

    for i in range(1, N):
        value, weight = details[i]
        for j in range(W + 1):
            if weight > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
    return dp[N - 1][W]


def tst(W: int, details: List[Tuple[int, int]], conflicts: List[Tuple[int, int]], expect: int):
    ans = solution(W, details, conflicts)
    print('[PASSED]' if ans == expect else '[FAILED]',
          f'W={W}, details={details}, conflictMap={conflictMap}, expect={expect}, output={ans}')


if __name__ == '__main__':
    tst(100, [(19, 20), (30, 20), (18, 20)], [(1, 2), (2, 3)], 37)
    tst(40, [(19, 20), (30, 20), (18, 20)], [(1, 2), (2, 3)], 49)
    tst(20, [(19, 20), (30, 20), (19, 20)], [(1, 2), (2, 3)], 30)
