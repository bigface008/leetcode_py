from typing import List

import utils


# https://leetcode.cn/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/description/?envType=daily-question&envId=2024-10-19
# class Solution:
#     def minOperations(self, nums: List[int]) -> int:
#         N = len(nums)
#         ans = 0
#         for i in range(N):
#             d = nums[i]
#             if d == 0:
#                 ans += 1
#                 for j in range(i, N):
#                     nums[j] = 1 - nums[j]
#         return ans

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        # 0 1 2 3 4 5
        # 0 0 0 0 0 0
        # 0 1 1 1 1 1
        # 0 1 0 0 0 0 -1
        ans = 0
        zero_cnt = 0
        for i in range(N):
            d = nums[i]
            if d == 0:
                if zero_cnt % 2 == 0:
                    ans += 1
                    zero_cnt += 1
            else:
                if zero_cnt % 2 == 1:
                    ans += 1
                    zero_cnt += 1
        return ans


def tst(nums: List[int], expect: int):
    output = Solution().minOperations(nums)
    utils.tst(f'min operations nums={nums}', output, expect)


if __name__ == '__main__':
    tst([0, 1, 1, 0, 1], 4)
    tst([1, 0, 0, 0], 1)
