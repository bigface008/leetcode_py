from typing import List

import utils


# https://leetcode.cn/problems/find-the-power-of-k-size-subarrays-i/?envType=daily-question&envId=2024-11-06
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        N = len(nums)
        ans = [-1] * (N - k + 1)
        cnt = 0
        for i, x in enumerate(nums):
            if i == 0 or nums[i - 1] + 1 == x:
                cnt += 1
            else:
                cnt = 1
            if cnt >= k:
                ans[i - k + 1] = x
        return ans


        # for i in range(k - 1):
        #     if nums[i] + 1 != nums[i + 1]:
        #         valid = False
        #         for j in range(k - 1):
        #             if i + j < len(ans):
        #                 ans[i + j] = -1
        #         break



class Solution2:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        N = len(nums)
        ans = [0] * (N - k + 1)
        increase = True
        for i in range(1, k):
            if nums[i] != nums[i - 1] + 1:
                ans[0] = -1
                increase = False
                break
        if not increase:
            return ans

        ans[0] = nums[k - 1]
        left = 1
        i = k
        while i < N:
            if nums[i] != nums[i - 1] + 1:
                for j in range(k - 1):
                    if left + j < N - k + 1:
                        ans[left + j] = -1
                i += k - 1
                left += k - 1
            else:
                ans[left] = nums[i]
                i += 1
                left += 1
        return ans


def tst(nums: List[int], k: int, expect: List[int]):
    output = Solution().resultsArray(nums, k)
    utils.tst(f'results nums={nums} k={k} epxect={expect}', output, expect)


if __name__ == '__main__':
    # tst([3, 2, 3, 2, 3, 2], 2, [-1, 3, -1, 3, -1])
    # tst([1, 4], 1, [1, 4])
    tst([3, 2, 43, 44, 45], 3, [-1, -1, 45])
