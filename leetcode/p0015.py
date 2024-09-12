from typing import List

import utils


# https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        N = len(nums)
        nums.sort()
        for i in range(N - 2):
            x = nums[i]
            if i > 0 and x == nums[i - 1]:
                continue
            j, k = i + 1, N - 1
            while j < k:
                y, z = nums[j], nums[k]
                curr_sum = x + y + z
                if curr_sum < 0:
                    j += 1
                elif curr_sum > 0:
                    k -= 1
                else:
                    ans.append([x, y, z])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return ans


def tst(nums: List[int], expect: List[List[int]]):
    output = Solution().threeSum(nums)
    utils.tst(f'3sum nums={nums}', output, expect)


if __name__ == '__main__':
    # tst([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]])
    tst([0, 0, 0], [[0, 0, 0]])
