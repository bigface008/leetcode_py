# https://leetcode.com/problems/count-covered-buildings/?envType=daily-question&envId=2025-12-11
from collections import defaultdict
from typing import List, Dict, Optional, Tuple


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        B = len(buildings)
        x_to_pts: Dict[int, List[int]] = defaultdict(list)
        y_to_pts: Dict[int, List[int]] = defaultdict(list)
        y_to_info: Dict[int, Tuple[int, int, int]] = dict()  # y -> (len, min, max)
        for i, (x, y) in enumerate(buildings):
            x_to_pts[x].append(i)
            y_to_pts[y].append(i)
        ans = 0
        for y, pts in y_to_pts.items():
            y_to_info[y] = (len(pts), min(buildings[pi][0] for pi in pts), max(buildings[pi][0] for pi in pts))
        for x, pts in x_to_pts.items():
            if len(pts) <= 2:
                continue
            pts.sort(key=lambda idx: buildings[idx][1])
            col_pt_cnt = len(pts)
            for i in range(1, col_pt_cnt - 1):
                by = buildings[pts[i]][1]
                same_y_num, same_y_min_x, same_y_max_x = y_to_info[by]
                if same_y_num <= 2:
                    continue
                if same_y_max_x != x and same_y_min_x != x:
                    ans += 1
        return ans


if __name__ == '__main__':
    print(Solution().countCoveredBuildings(3, [[1, 2], [2, 2], [3, 2], [2, 1], [2, 3]]))
