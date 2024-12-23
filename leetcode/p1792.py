# https://leetcode.com/problems/maximum-average-pass-ratio/?envType=daily-question&envId=2024-12-15
import heapq
from typing import List

import utils


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        pq = [(p / t - (p + 1) / (t + 1), p, t) for p, t in classes]
        heapq.heapify(pq)
        while extraStudents:
            diff, p, t = pq[0]
            extraStudents -= 1
            heapq.heappop(pq)
            heapq.heappush(pq, (((p + 1) / (t + 1) - (p + 2) / (t + 2)), p + 1, t + 1))
        return sum(p / t for _, p, t in pq) / len(pq)


        # pq = [(p / t, p, t) for p, t in classes]
        # heapq.heapify(pq)
        # while extraStudents != 0:
        #     ratio, p, t = pq[0]
        #     extraStudents -= 1
        #     # heapq.heapreplace(pq, ((p + 1) / t, p + 1, t))
        #     heapq.heappop(pq)
        #     heapq.heappush(pq, ((p + 1) / (t + 1), p + 1, t + 1))
        # return sum(r for r, _, _ in pq) / len(pq)


def check(classes: List[List[int]], extraStudents: int, expect: float):
    output = Solution().maxAverageRatio(classes, extraStudents)
    utils.tst(f'classes={classes} extraStudents={extraStudents}', output, expect)


if __name__ == '__main__':
    check([[1, 2], [3, 5], [2, 2]], 2, 0.78333)