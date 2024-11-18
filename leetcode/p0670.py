# https://leetcode.com/problems/maximum-swap/?envType=daily-question&envId=2024-10-17
from itertools import accumulate

import utils


class Solution:
    def maximumSwap(self, num: int) -> int:
        temp = num
        arr = []
        while temp > 0:
            d = temp % 10
            arr.append(d)
            temp //= 10
        arr.reverse()
        N = len(arr)
        ans = num
        for i in range(N):
            mx = arr[i]
            mx_i = i
            for j in range(i + 1, N):
                if arr[j] >= mx:
                    mx = arr[j]
                    mx_i = j
            if arr[i] < mx:
                arr[i], arr[mx_i] = arr[mx_i], arr[i]
                res = 0
                for k, d in enumerate(arr):
                    res += d * pow(10, len(arr) - k - 1)
                arr[i], arr[mx_i] = arr[mx_i], arr[i]
                ans = max(ans, res)
        return ans

        # max_d = 0
        # max_i = -1
        # temp = num
        # arr = []
        # while temp > 0:
        #     d = temp % 10
        #     if d > max_d:
        #         max_d = d
        #         max_i = len(arr)
        #     arr.append(d)
        #     temp //= 10
        # arr.reverse()
        # if max_i == -1 or max_d == arr[0]:
        #     return num
        # max_i = len(arr) - max_i - 1
        # arr[0], arr[max_i] = arr[max_i], arr[0]
        # # return accumulate([d * pow(10, len(arr) - i - 1) for i, d in enumerate(arr)], initial=0)
        # res = 0
        # for i, d in enumerate(arr):
        #     res += d * pow(10, len(arr) - i - 1)
        # return res


def tst(num: int, expect: int):
    output = Solution().maximumSwap(num)
    utils.tst(f'num={num}', output, expect)


if __name__ == '__main__':
    # tst(2736, 7236)
    # tst(12, 21)
    # tst(98368, 98863)
    tst(1993, 9913)