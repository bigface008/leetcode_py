# 给定一个数组nums，每个元素nums[i]代表横坐标i和i+1之间有一个高为nums[i]的长方形，求这些长方形的下方区域所能构成的最大长方形的面积。
from itertools import permutations
from string import ascii_lowercase
from typing import List

import utils


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        min_stk = []
        max_area = [0] * N
        for i, h in enumerate(heights):
            while min_stk and heights[min_stk[-1]] >= h:
                j = min_stk[-1]
                max_area[j] += heights[j] * (i - j - 1)
                min_stk.pop()
            wl = (i - min_stk[-1] - 1) if min_stk else i
            max_area[i] = h + wl * h
            min_stk.append(i)
        for i in min_stk:
            max_area[i] += heights[i] * (N - 1 - i)
        return max(max_area)



class Solution3:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        max_area = [0] * N
        min_stk1 = []
        for i, h in enumerate(heights):
            while min_stk1 and heights[min_stk1[-1]] >= h:
                min_stk1.pop()
            width = (i - min_stk1[-1] - 1) if min_stk1 else i
            # print(f'i={i} h={h} width={width} min_stk1={min_stk1} area={h * width}')
            max_area[i] = h * width + h
            min_stk1.append(i)
        min_stk2 = []
        ans = heights[0]
        for i in range(N - 1, -1, -1):
            h = heights[i]
            while min_stk2 and heights[min_stk2[-1]] >= h:
                min_stk2.pop()
            width = (min_stk2[-1] - i - 1) if min_stk2 else (N - 1 - i)
            # print(f'i={i} h={h} width={width} min_stk2={min_stk2} area={h * width}')
            max_area[i] += h * width
            ans = max(ans, max_area[i])
            min_stk2.append(i)
        # print(f'max_area={max_area}')
        return ans


class Solution2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        min_stk = []
        ans = 0
        for i, x in enumerate(heights):
            while min_stk and heights[min_stk[-1]] >= x:
                min_stk.pop()
            min_stk.append(i)
            # print(f'i={i}, x={x}, min_stk={min_stk}')
            for idx, j in enumerate(min_stk):
                width = (i + 1) if idx == 0 else (i - min_stk[idx - 1])
                area = width * heights[j]
                # print(f'  i={i}, j={j}, width={width}, height={heights[j]} area={area}')
                ans = max(ans, area)
        return ans


def solution(nums: List[int]) -> int:
    min_stk = []
    ans = 0
    for i, x in enumerate(nums):
        while min_stk and nums[min_stk[-1]] > x:
            min_stk.pop()
        for j in min_stk:
            ans = max(ans, (i - j + 1) * nums[j])
        min_stk.append(i)
    return ans


def check(nums: List[int], expect: int):
    output = Solution().largestRectangleArea(nums)
    utils.tst(f'solution({nums})', output, expect)


if __name__ == '__main__':
    # check([2, 1, 5, 6, 2, 3], 10)
    # check([2, 3], 4)
    # check([2, 4], 4)
    # check([1], 1)
    # check([2, 1, 2], 3)
    # check([4, 2, 0, 3, 2, 5], 6)
    print(list(permutations(ascii_lowercase, 2)))
