import bisect
from collections import defaultdict
from typing import List, Tuple

import utils


# https://leetcode.cn/problems/find-the-median-of-the-uniqueness-array/?envType=daily-question&envId=2024-08-27
class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        N = len(nums)
        K = (N * (N + 1) // 2 + 1) // 2

        def check(upper: int) -> bool:
            cnt, l = 0, 0
            freq = defaultdict(int)
            for r, x in enumerate(nums):
                freq[x] += 1
                while len(freq) > upper:
                    drop = nums[l]
                    freq[drop] -= 1
                    if freq[drop] == 0:
                        del freq[drop]
                    l += 1
                cnt += r - l + 1
                if cnt >= K:
                    return True
            return False

        return bisect.bisect_left(range(1, len(set(nums))), True, key=check) + 1

        # l, r = 0, len(set(nums))
        # while l + 1 < r:
        #     mid = (l + r) // 2
        #     if check(mid):
        #         r = mid
        #     else:
        #         l = mid
        # return r

        # def countSubLessThan(threshold: int) -> Tuple[int, int]:
        #     ans_l, ans_r = 0, 0
        #     left, right = 0, 0
        #     dst = defaultdict(int)
        #     while right < N:
        #         dst[nums[right]] += 1
        #         while len(dst) > threshold and left <= right:
        #             tmp = nums[left]
        #             if dst[tmp] == 1:
        #                 dst.pop(tmp)
        #             else:
        #                 dst[tmp] -= 1
        #             left += 1
        #         ans_r += right - left + 1
        #         tmp_left = left
        #         while len(dst) == threshold and left <= right:
        #             tmp = nums[left]
        #             if dst[tmp] == 1:
        #                 dst.pop(tmp)
        #             else:
        #                 dst[tmp] -= 1
        #             left += 1
        #         ans_l += right - left + 1
        #         right += 1
        #     return ans_l, ans_r
        #
        # start, end = 1, len(set(nums))
        # target = N * (N + 1) // 2
        # if target % 2 == 0:
        #     target = target // 2 - 1
        # else:
        #     target = target // 2
        # while start <= end:
        #     mid = (start + end) // 2
        #     cnt_l, cnt_r = countSubLessThan(mid)
        #     print(f'cnt_l={cnt_l} cnt_r={cnt_r} mid={mid} target={target}')
        #     if cnt_l <= target < cnt_r:
        #         return mid
        #     elif target < cnt_l:
        #         end -= 1
        #     else:
        #         start += 1
        # return -1  # ?

        # def countSubLessThan(threshold: int) -> Tuple[int, int]:
        #     ans_l, ans_r = 0, 0
        #     left, right = 0, 0
        #     dst = defaultdict(int)
        #     while right < N:
        #         while len(dst) > threshold and left <= right:
        #             tmp = nums[left]
        #             if dst[tmp] == 1:
        #                 dst.pop(tmp)
        #             else:
        #                 dst[tmp] -= 1
        #             left += 1
        #         while len(dst) == threshold and left <= right:
        #             pass
        #         ans_r += right - left + 1
        #         dst[nums[right]] += 1
        #         right += 1
        #     return ans_l, ans_r
        #
        # start, end = 1, len(set(nums))
        # target = int(N * (N + 1) / 2)
        # if target % 2 == 0:
        #     target = target // 2 - 1
        # else:
        #     target = target // 2
        # while start <= end:
        #     mid = (start + end) // 2
        #     cnt = countSubLessThan(mid)
        #     print(f'cnt={cnt} mid={mid}')
        #     if target == cnt:
        #         return mid
        #     elif target < cnt:
        #         end -= 1
        #     else:
        #         start += 1
        # return -1 # ?


def tst(nums: List[int], expect: int):
    output = Solution().medianOfUniquenessArray(nums)
    utils.tst(f'median of uniqueness array nums={nums}', output, expect)


if __name__ == '__main__':
    tst([1, 2, 3], 1)
    tst([3, 4, 3, 4, 5], 2)
    tst([85, 4, 85, 4], 2)
    tst([46, 73, 46, 46, 46], 1)
