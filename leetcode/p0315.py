from typing import List
import bisect

import utils


# https://leetcode.cn/problems/count-of-smaller-numbers-after-self/
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [0] * N
        indices = list(range(N))
        temp = indices.copy()

        def dfs(left: int, right: int):
            if left == right:
                return
            if left + 1 == right:
                if nums[indices[left]] > nums[indices[right]]:
                    ans[indices[left]] += 1
                    tmp = indices[left]
                    indices[left] = indices[right]
                    indices[right] = tmp
                return

            mid = (left + right) // 2
            dfs(left, mid)
            dfs(mid + 1, right)
            if nums[indices[mid]] < nums[indices[mid + 1]]:
                return

            for i in range(left, right + 1):
                temp[i] = indices[i]
            i, j = left, mid + 1
            k = left
            while i <= mid and j <= right:
                if nums[temp[i]] <= nums[temp[j]]:
                    indices[k] = temp[i]
                    ans[indices[k]] += j - mid - 1
                    i += 1
                else:
                    indices[k] = temp[j]
                    j += 1
                k += 1
            while i <= mid:
                indices[k] = temp[i]
                ans[indices[k]] += right - mid
                i += 1
                k += 1
            while j <= right:
                indices[k] = temp[j]
                j += 1
                k += 1

        dfs(0, N - 1)
        return ans


def tst(nums: List[int], expect: List[int]):
    output = Solution().countSmaller(nums)
    utils.tst(f'count smaller nums={nums}', output, expect)


if __name__ == '__main__':
    # tst([5, 2, 6, 1], [2, 1, 1, 0])
    tst([0, 2, 1], [0, 1, 0])
