from typing import List

import utils


# https://leetcode.cn/problems/maximize-win-from-two-segments/?envType=daily-question&envId=2024-09-11
class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        N = len(prizePositions)
        mx = [0] * (N + 1)
        ans = 0
        left = 0
        for right, x in enumerate(prizePositions):
            while x - prizePositions[left] > k:
                left += 1
            ans = max(ans, mx[left] + right - left + 1)
            mx[right + 1] = max(mx[right], right - left + 1)
        return ans

    # def maximizeWin(self, prizePositions: List[int], k: int) -> int:
    #     wd_cnt = 0
    #     N = len(prizePositions)
    #     left = 0
    #     max1_wd_cnt, max2_wd_cnt = 0, 0
    #     for right, x in enumerate(prizePositions):
    #         wd_cnt += 1
    #         while prizePositions[left] + k < x:
    #             left += 1
    #             wd_cnt -= 1
    #         if wd_cnt > max1_wd_cnt:
    #             max2_wd_cnt = max1_wd_cnt
    #             max1_wd_cnt = wd_cnt
    #         elif wd_cnt > max2_wd_cnt:
    #             max2_wd_cnt = wd_cnt
    #     return max1_wd_cnt + max2_wd_cnt


def tst(prizePositions: List[int], k: int, expect: int):
    output = Solution().maximizeWin(prizePositions, k)
    utils.tst(f'max win prizePositions={prizePositions} k={k}', output, expect)


if __name__ == '__main__':
    tst([1, 1, 2, 2, 3, 3, 5], 2, 7)
    tst([1, 2, 3, 4], 0, 2)
