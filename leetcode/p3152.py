from typing import List
from itertools import accumulate
import utils


# https://leetcode.cn/problems/special-array-ii/?envType=daily-question&envId=2024-08-14
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        ans = [False for _ in queries]
        preSum = list(accumulate([0 if nums[i] % 2 != nums[i + 1] % 2 else 1 for i in range(len(nums) - 1)], initial=0))
        for i, q in enumerate(queries):
            l, r = q
            ans[i] = preSum[r] - preSum[l] == 0
        return ans





# class Solution:
#     def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
#         ans = [False for _ in queries]
#         start, end = len(nums) - 1, 0
#         for q in queries:
#             start = min(start, q[0])
#             end = max(end, q[1])
#         queries.sort()
#
#         specialRanges = []
#         left = 0
#         isSpecial = False
#         for i in range(start, end):
#             if nums[i] % 2 == nums[i + 1] % 2:
#                 if isSpecial:
#                     isSpecial = False
#                     if left != i:
#                         specialRanges.append((left, i))
#             else:
#                 if not isSpecial:
#                     left = i
#                     isSpecial = True
#         print(specialRanges)
#
#         i = 0
#         for j, q in enumerate(queries):
#             l, r = q
#             while i < len(specialRanges):
#                 if specialRanges[i][1] <= l:
#                     i += 1
#                 else:
#                     if specialRanges[i][0] > r:
#                         ans[j] = False
#                     else:
#                         ans[j] = True
#         return ans


def tst(nums: List[int], queries: List[List[int]], expect: List[bool]):
    output = Solution().isArraySpecial(nums, queries)
    utils.tst(f'isArraySpecial nums={nums} queries={queries}', output, expect)


if __name__ == '__main__':
    # tst([3,4,1,2,6], [[0,4]], [False])
    # tst([4,3,1,6], [[0,2],[2,3]], [False, True])
    ds = [1, 2, 3, 4, 5]
    s = list(accumulate(ds, initial=0))
    print(s)

# class Solution:
#     def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
#         ans = [False for _ in queries]
#         queries.sort()
#
#         def isSpecial(l, r):
#             for i in range(l, r):
#                 if nums[i] % 2 == nums[i + 1] % 2:
#                     return False
#             return True
#
#         ans[0] = isSpecial(queries[0][0], queries[0][1])
#
#         for i in range(1, len(queries)):
#             pLeft, pRight = queries[i - 1]
#             left, right = queries[i]
#             if left >= pRight: # no overlap
#                 ans[i] = isSpecial(left, right)
#             else:
#                 if right <= pRight:
#                     pass
#                 else:
#                     start = left
#                     if ans[i - 1]:
#                         start = pRight
#                     ans[i] = isSpecial(start, right)
#         return ans