from typing import List
from math import inf


# https://leetcode.com/problems/trapping-rain-water/description/
class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        left, right = 0, N - 1
        leftMax, rightMax = 0, 0
        ans = 0
        while left <= right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if leftMax < rightMax:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1
        return ans

        # monoStk = []
        # ans = 0
        # for i, h in enumerate(height):
        #     while monoStk and height[monoStk[-1]] <= h:
        #         bottomH = height[monoStk.pop()]
        #         if not monoStk:
        #             break
        #         leftI = monoStk[-1]
        #         dh = min(height[leftI], h) - bottomH
        #         ans += dh * (i - leftI - 1)
        #     monoStk.append(i)
        # return ans


if __name__ == '__main__':
    print(Solution().trap([3, 2, 1, 0, 1, 2, 3]))