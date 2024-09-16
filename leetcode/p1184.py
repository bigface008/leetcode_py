from typing import List


# https://leetcode.cn/problems/distance-between-bus-stops/?envType=daily-question&envId=2024-09-16
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        dist_sum = sum(distance)
        if destination < start:
            start, destination = destination, start
        path_sum = 0
        for i in range(start, destination):
            path_sum += distance[i]
        remain = dist_sum - path_sum
        return min(remain, path_sum)