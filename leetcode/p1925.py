# https://leetcode.com/problems/count-square-sum-triples/?envType=daily-question&envId=2025-12-08
import math
from collections import defaultdict
from typing import List, Dict, Tuple, Optional


class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for c in range(n, 0, -1):
            for a in range(1, c):
                target = c * c - a * a
                b = int(math.sqrt(target))
                if b * b == target:
                    if b == a:
                        ans += 1
                    elif b < a:
                        break
                    else:
                        ans += 2
        return ans


if __name__ == '__main__':
    print(Solution().countTriples(5))
