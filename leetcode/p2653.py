from typing import List


class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        pass

        # def partition(arr: List[int], start: int, end: int) -> int:
        #     pivot = arr[start]
        #     while start < end:
        #         while start < end and pivot <= arr[end]:
        #             end -= 1
        #         arr[start] = arr[end]
        #         while start < end and arr[start] <= pivot:
        #             start += 1
        #         arr[end] = arr[start]
        #     arr[start] = pivot
        #     return start
        #
        # def _quickSelect(arr: List[int], start: int, end: int, x: int):
        #     pivotIdx = partition(arr, start, end)
        #     if pivotIdx == x:
        #         return
        #     elif pivotIdx > x:
        #         _quickSelect(arr, start, pivotIdx - 1, x)
        #     else:
        #         _quickSelect(arr, pivotIdx + 1, start, x)
