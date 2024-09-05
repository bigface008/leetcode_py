from typing import List


# https://leetcode.cn/problems/car-pooling/
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_to = 0
        for _, _, t in trips:
            max_to = max(max_to, t + 1)
        path = [0] * max_to
        for n, f, t in trips:
            path[f] += n
            path[t] -= n
        ans = 0
        for p in path:
            ans += p
            if ans > capacity:
                return False
        return True


if __name__ == '__main__':
    d = {12: '12', 1: '1', -1: '-1', 5: '5', 22: '22', 3: '3', 19: '19'}
    print(d)
    print(sorted(d))
    print(d.keys())