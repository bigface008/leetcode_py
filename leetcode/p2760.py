# https://leetcode.cn/problems/longest-even-odd-subarray-with-threshold/description/
from typing import List, Dict, Tuple, Set


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans = 0
        N = len(nums)
        i = 0
        while i < N:
            if nums[i] > threshold or nums[i] % 2 == 1:
                i += 1
                continue
            start = i
            while i < N and nums[i] <= threshold:
                if i + 1 >= N:
                    i += 1
                    break
                if nums[i] % 2 == nums[i + 1] % 2:
                    i += 1
                    break
                i += 1
            ans = max(ans, i - start)
        return ans


if __name__ == "__main__":
    # print(Solution().longestAlternatingSubarray([3, 2, 5, 4], 5))
    print(Solution().longestAlternatingSubarray([2, 3, 4, 5], 4))
