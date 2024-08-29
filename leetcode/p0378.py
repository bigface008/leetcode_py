from typing import List
import bisect

from hvplot import output

import utils


# https://leetcode.cn/problems/kth-smallest-element-in-a-sorted-matrix/
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        N = len(matrix)

        def check(threshold: int) -> bool:
            i, j = N - 1, 0
            ans = 0
            while i >= 0 and j < N:
                if matrix[i][j] <= threshold:
                    ans += i + 1
                    if ans >= k:
                        return True
                    j += 1
                else:
                    i -= 1
            return False

        return bisect.bisect_left(range(matrix[0][0], matrix[-1][-1]), True, key=check) + matrix[0][0]

        # l, r = matrix[0][0], matrix[-1][-1]
        # while l < r:
        #     mid = (l + r) // 2
        #     if count(mid) >= k:
        #         r = mid
        #     else:
        #         l = mid + 1
        # return l

        # while l <= r:
        #     tmp = (l + r) // 2
        #     cnt = count(tmp)
        #     print(f'l={l} r={r} tmp={tmp} cnt={cnt}')
        #     if cnt == k:
        #         return tmp
        #     elif cnt > k:
        #         r -= 1
        #     else:
        #         l += 1
        # return -1


def tst(matrix: List[List[int]], k: int, expect: int):
    output = Solution().kthSmallest(matrix, k)
    utils.tst(f'kth smallest matrix={matrix} k={k}', output, expect)


if __name__ == '__main__':
    tst([[1, 2], [1, 3]], 1, 1)
