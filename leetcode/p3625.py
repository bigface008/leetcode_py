# https://leetcode.cn/problems/count-number-of-trapezoids-ii/description/?envType=daily-question&envId=2025-12-03
from collections import defaultdict
from typing import List, Dict, Optional, Tuple
from math import inf


# k * x1 * x2 + b * x2 = y1 * x2
# k * x2 * x1 + b * x1 = y2 * x1
# b * (x2 - x1) = y1 * x2 - y2 * x1
# b = (y1 * x2 - y2 * x1) / (x2 - x1)


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        k_to_b_to_pairs: Dict[float, Dict[float, int]] = defaultdict(dict)
        x_to_pairs: Dict[float, int] = defaultdict(int)
        middle_to_k_to_pairs: Dict[Tuple[int, int], Dict[float, int]] = defaultdict(dict)
        N = len(points)
        for i, (x1, y1) in enumerate(points):
            for j in range(i + 1, N):
                x2, y2 = points[j]
                if i == j:
                    continue
                mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                if x1 == x2:
                    k = inf
                    x_to_pairs[x1] += 1
                else:
                    k = (y1 - y2) / (x1 - x2)
                    b = (y1 * x2 - y2 * x1) / (x2 - x1)
                    if b in k_to_b_to_pairs[k]:
                        k_to_b_to_pairs[k][b] += 1
                    else:
                        k_to_b_to_pairs[k][b] = 1
                if k in middle_to_k_to_pairs[(mx, my)]:
                    middle_to_k_to_pairs[(mx, my)][k] += 1
                else:
                    middle_to_k_to_pairs[(mx, my)][k] = 1

        ans = 0
        for k, b_to_pairs in k_to_b_to_pairs.items():
            acc = 0
            for b, pairs in b_to_pairs.items():
                ans += acc * pairs
                acc += pairs
        acc = 0
        for x, pairs in x_to_pairs.items():
            ans += acc * pairs
            acc += pairs

        px_cnt = 0
        for middle, k_to_pairs in middle_to_k_to_pairs.items():
            acc = 0
            for k, pairs in k_to_pairs.items():
                px_cnt += pairs * acc
                acc += pairs
        ans -= px_cnt
        return ans


if __name__ == '__main__':
    print(Solution().countTrapezoids([[71, -89], [-75, -89], [-9, 11], [-24, -89], [-51, -89], [-77, -89], [42, 11]]))
    # print(Solution().countTrapezoids([[-3, 2], [3, 0], [2, 3], [3, 2], [2, -3]]))
