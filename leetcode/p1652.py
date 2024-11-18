from typing import List

from itertools import accumulate

import utils


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        ans = [0] * N
        pre_sum = list(accumulate(code, initial=0))
        for i in range(N):
            res = 0
            if k > 0:
                if i + k < N:
                    res = pre_sum[i + k + 1] - pre_sum[i + 1]
                else:
                    res = pre_sum[-1] - pre_sum[i + 1] + pre_sum[i + k - N + 1] - pre_sum[0]
            elif k < 0:
                k = -k
                if i - k >= 0:
                    res = pre_sum[i] - pre_sum[i - k]
                else:
                    res = pre_sum[i] - pre_sum[0] + pre_sum[-1] - pre_sum[i - k - 1]
                k = -k
            else:
                res = 0
            ans[i] = res
        return ans


def tst(code: List[int], k: int, expect: List[int]):
    output = Solution().decrypt(code, k)
    utils.tst(f'test {code} {k}', output, expect)


if __name__ == '__main__':
    # tst([5, 7, 1, 4], 3, [12, 10, 16, 13])
    tst([2, 4, 9, 3], -2, [12, 5, 6, 13])
