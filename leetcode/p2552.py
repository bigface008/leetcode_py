from typing import List

import utils


# https://leetcode.cn/problems/count-increasing-quadruplets/?envType=daily-question&envId=2024-09-10
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        N = len(nums)
        great = [[0] * (N + 1) for _ in range(N)]
        # great[-1] = [0] * (N + 1)
        for k in range(N - 2, 1, -1):
            great[k] = great[k + 1].copy()
            for x in range(1, nums[k + 1]):
                great[k][x] += 1

        ans = 0
        less = [0] * (N + 1)
        for j in range(1, N - 1):
            for x in range(nums[j - 1] + 1, N + 1):
                less[x] += 1
            for k in range(j + 1, N - 1):
                if nums[j] > nums[k]:
                    ans += less[nums[k]] * great[k][nums[j]]
        return ans



def tst(nums: List[int], expect: int):
    # assert Solution().countQuadruplets(nums) == expect
    output = Solution().countQuadruplets(nums)
    utils.tst(f'nums={nums}', output, expect)


if __name__ == '__main__':
    # tst([1, 3, 2, 4, 5], 2)
    tst([2, 5, 3, 1, 4], 0)
