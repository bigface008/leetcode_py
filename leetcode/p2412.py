# https://leetcode.cn/problems/minimum-money-required-before-transactions/?envType=daily-question&envId=2025-01-25
import heapq
from typing import List

import utils


# [2, 1] [5, 0] [6 1]
# 7
# [5, 0] [6, 1]
# [5, 0] [2, 1] ,[4, 2]
# 10


# [5, 0] [4, 2]
# 9 [5, 0] [4, 2]

# [5, 0] [2, 1]
# 7 [5, 0] [2, 1]
# 6 [2, 1] [5, 0]

# [4, 2] [2, 1]
# 5 [2, 1] [4, 2] diff + cost  1 4
# 4 [4, 2] [2, 1]              2 2

# 10 [5, 0] [2, 1] [4, 2]      6 4
#

# ANS
# ANS - diff_sum = 0
# ANS - diff = last


class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        N = len(transactions)
        lose_sum = 0
        mx = 0
        for cost, cashback in transactions:
            lose_sum += max(0, cost - cashback)
            mx = max(mx, min(cost, cashback))
        return lose_sum + mx

        # diff_sum = sum(cost - cashback for cost, cashback in transactions)
        # pq = [(-(cost + diff_sum - (cost - cashback)), i) for i, (cost, cashback) in enumerate(transactions)]
        # heapq.heapify(pq)
        # remain_diff_sum = diff_sum
        # ans = 0
        # while pq:
        #     val, i = heapq.heappop(pq)
        #     cost, cashback = transactions[i]
        #     remain_diff_sum -= (cost - cashback)
        #     ans = max(ans, cost + remain_diff_sum)
        # return ans



class Solution2:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        N = len(transactions)

        # for each element
        #   cost, cashback
        #   cost + diff_sum - (cost - cashback) TODO
        diff_sum = sum(cost - cashback for cost, cashback in transactions)
        # pq = [(cost + diff_sum - (cost - cashback)) for cost, cashback in transactions]

        for i, (cost, cashback) in enumerate(transactions):
            print(f'i={i} val={cost + diff_sum - (cost - cashback)} cost={cost} cashback={cashback}')

        ans = max((cost + diff_sum - (cost - cashback)) for cost, cashback in transactions)
        return ans

        # transactions.sort(key=lambda t: -t[0])
        # # transactions.sort(key=lambda t: (t[1] - t[0], -t[0]))
        # # transactions.sort(key=lambda t: (t[0] - t[1], t[0]))
        # ans = transactions[0][0]
        # for i in range(1, N):
        #     cost, cashback = transactions[i]
        #     ans -= cashback - cost
        #     ans = max(ans, cost)
        # return ans


def check(transactions: List[List[int]], expect: int):
    output = Solution().minimumMoney(transactions)
    utils.tst(f'transactions={transactions}', output, expect)


if __name__ == '__main__':
    # check([[2, 1], [5, 0], [4, 2]], 10)
    check([[7, 2], [0, 10], [5, 0], [4, 1], [5, 8], [5, 9]], 18)
    check([[7, 2], [5, 0], [4, 1]], 18)
    # 15 [5, 0] [4, 1] [7, 2] 5
    #
