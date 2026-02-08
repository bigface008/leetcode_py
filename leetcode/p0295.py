# https://leetcode.cn/problems/find-median-from-data-stream/
from sortedcontainers import SortedList
from typing import List, Dict
import heapq


class MedianFinder:

    def __init__(self):
        self.left: List[int] = []
        self.right: List[int] = []

    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right):
            right_min = heapq.heappushpop(self.right, num)
            heapq.heappush(self.left, -right_min)
        else:
            left_max = heapq.heappushpop(self.left, -num)
            heapq.heappush(self.right, left_max)

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        else:
            return -self.left[0]


# class MedianFinder:
#
#     def __init__(self):
#         self.left: List[int] = []
#         self.right: List[int] = []
#
#     def addNum(self, num: int) -> None:
#         if len(self.left) == len(self.right):
#             heapq.heappush(self.right, num)
#             right_min = self.right[0]
#             heapq.heappop(self.right)
#             heapq.heappush(self.left, -right_min)
#         else:
#             heapq.heappush(self.left, -num)
#             left_max = -self.left[0]
#             heapq.heappop(self.left)
#             heapq.heappush(self.right, left_max)
#
#     def findMedian(self) -> float:
#         if len(self.left) == len(self.right):
#             return (-self.left[0] + self.right[0]) / 2
#         else:
#             return -self.left[0]


# class MedianFinder:
#
#     def __init__(self):
#         self.arr = SortedList()
#
#     def addNum(self, num: int) -> None:
#         self.arr.add(num)
#
#     def findMedian(self) -> float:
#         N = len(self.arr)
#         if N % 2 == 0:
#             return (self.arr[N // 2] + self.arr[N // 2 - 1]) / 2
#         else:
#             return self.arr[N // 2]


if __name__ == '__main__':
    f = MedianFinder()
    f.addNum(1)
    f.addNum(2)
    print(f.findMedian())