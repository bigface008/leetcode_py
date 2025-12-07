# https://leetcode.com/problems/count-collisions-on-a-road/?envType=daily-question&envId=2025-12-04
class Solution:
    def countCollisions(self, directions: str) -> int:
        N = len(directions)
        ans = 0
        moving_r_count = 0
        prev_r_pos = -1
        prev_s_pos = -1
        for i, d in enumerate(directions):
            if d == 'R':
                moving_r_count += 1
                prev_r_pos = i
            elif d == 'L':
                if prev_s_pos != -1 or prev_r_pos != -1:
                    ans += 1
                ans += moving_r_count
                moving_r_count = 0
            else:
                prev_s_pos = i
                ans += moving_r_count
                moving_r_count = 0
        return ans