import collections
from typing import List


# https://leetcode.com/problems/permutations-ii/
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        ans = []
        path = []
        counter = collections.Counter()
        for x in nums:
            counter[x] += 1

        def backtrack(pos: int):
            if pos == N:
                ans.append(path.copy())
                return
            for i, x in enumerate(nums):
                if i > 0 and x == nums[i - 1]:
                    continue
                if counter[x]:
                    path.append(x)
                    counter[x] -= 1
                    backtrack(pos + 1)
                    path.pop()
                    counter[x] += 1

        backtrack(0)
        return ans
