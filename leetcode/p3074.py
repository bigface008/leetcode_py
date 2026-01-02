# https://leetcode.com/problems/apple-redistribution-into-boxes/description/?envType=daily-question&envId=2025-12-24
import heapq
from typing import List, Dict, Tuple, Optional


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apple_cnt = sum(apple)
        caps = [-c for c in capacity]
        heapq.heapify(caps)
        ans = 0
        while caps:
            box = -caps[0]
            if apple_cnt >= box:
                apple_cnt -= box
                ans += 1
            elif apple_cnt > 0:
                ans += 1
                break
            heapq.heappop(caps)
        return ans


if __name__ == '__main__':
    # print(Solution().minimumBoxes([5, 5, 5], [2, 4, 2, 7]))
    # print(Solution().minimumBoxes([1, 3, 2], [4, 3, 1, 5, 2]))
    print(Solution().minimumBoxes([9, 8, 8, 2, 3, 1, 6], [10, 1, 4, 10, 8, 5]))
