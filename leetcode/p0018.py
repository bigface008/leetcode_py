from typing import List


# https://leetcode.com/problems/4sum/
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        ans = []
        for i in range(N - 3):
            x = nums[i]
            if i > 0 and x == nums[i - 1]:
                continue
            for j in range(i + 1, N - 2):
                y = nums[j]
                if j > i + 1 and y == nums[j - 1]:
                    continue
                k0, k1 = j + 1, N - 1
                while k0 < k1:
                    z0, z1 = nums[k0], nums[k1]
                    curr_sum = x + y + z0 + z1
                    if curr_sum < target:
                        k0 += 1
                    elif curr_sum > target:
                        k1 -= 1
                    else:
                        ans.append([x, y, z0, z1])
                        k0 += 1
                        k1 -= 1
                        while k0 < k1 and nums[k0] == nums[k0 - 1]:
                            k0 += 1
                        while k0 < k1 and nums[k1] == nums[k1 + 1]:
                            k1 -= 1
        return ans