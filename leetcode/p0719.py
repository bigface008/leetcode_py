from typing import List
import utils
import bisect


# https://leetcode.cn/problems/find-k-th-smallest-pair-distance/description/
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        def count(threshold: int) -> int:
            cnt, left = 0, 0
            for right in range(1, len(nums)):
                while nums[right] - nums[left] > threshold:
                    left += 1
                cnt += right - left
            return cnt

        return bisect.bisect_left(range(nums[-1] - nums[0] + 1), k, key=count)


def tst(nums: List[int], k: int, expect: int):
    output = Solution().smallestDistancePair(nums, k)
    utils.tst(f'smallestDistancePair nums={nums} k={k}', output, expect)


if __name__ == '__main__':
    # tst([1, 3, 1], 1, 0)
    # tst([1, 1, 1], 2, 0)
    # tst([1, 6, 1], 3, 5)
    print(list(range(10)))
