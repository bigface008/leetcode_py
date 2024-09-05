from typing import List

import utils


# https://leetcode.com/problems/find-missing-observations/description/?envType=daily-question&envId=2024-09-05
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        M = len(rolls)
        n_sum = mean * (M + n) - sum(rolls)
        if n_sum > 6 * n or n_sum < n:
            return []
        elif n_sum == 6 * n:
            return [6] * n
        n_avg = n_sum // n
        ans = [n_avg] * n
        curr_sum = n_avg * n
        if curr_sum == n_avg:
            return ans
        for i in range(n):
            tmp = ans[i]
            ans[i] += n_sum - curr_sum
            if ans[i] <= 6:
                break
            curr_sum += 6 - tmp
            ans[i] = 6
        return ans


# class Solution:
#     def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
#         M = len(rolls)
#         n_sum = mean * (M + n) - sum(rolls)
#         if n_sum > 6 * n:
#             return []
#         elif n_sum == 6 * n:
#             return [6] * n
#         ans = []
#         curr = []
#
#         def dfs(i: int, remain: int):
#             if i == n:
#                 if remain == 0:
#                     nonlocal ans
#                     if not ans:
#                         ans = curr.copy()
#                 return
#             if remain <= 0:
#                 return
#             for j in range(6, 0, -1):
#                 nr = remain - j
#                 if nr >= n - 1 - i:
#                     curr.append(j)
#                     dfs(i + 1, nr)
#                     curr.pop()
#
#         dfs(0, n_sum)
#         return ans


def tst(rolls: List[int], mean: int, n: int, expect: List[int]):
    output = Solution().missingRolls(rolls, mean, n)
    utils.tst(f'rolls={rolls} mean={mean} n={n}', output, expect)


if __name__ == '__main__':
    tst([1, 5, 6], 3, 4, [2, 3, 2, 2])
