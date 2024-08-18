from typing import List
from math import inf

# https://leetcode.com/problems/maximum-distance-in-arrays/description/?envType=daily-question&envId=2024-08-16
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        N = len(arrays)
        max1, max2 = -1, -1
        min1, min2 = -1, -1
        maxValues = [0] * N
        minValues = [0] * N
        for i, arr in enumerate(arrays):
            maxValues[i] = max(arr)
            minValues[i] = min(arr)
            if maxValues[max1] < maxValues[i] or max1 == -1:
                max2 = max1
                max1 = i
            elif maxValues[max2] < maxValues[i] or max2 == -1:
                max2 = i
            if minValues[min1] > minValues[i] or min1 == -1:
                min2 = min1
                min1 = i
            elif minValues[min2] > minValues[i] or min2 == -1:
                min2 = i
        if min1 != max1:
            return maxValues[max1] - minValues[min1]
        else:
            return max(maxValues[max1] - minValues[min2], maxValues[max2] - minValues[min1])


if __name__ == '__main__':
    print(Solution().maxDistance([[1, 5], [3, 4]]) == 3)
