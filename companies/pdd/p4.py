import sys
import heapq
from collections import defaultdict
from email.policy import default
from math import inf
import bisect

N, M = [int(s) for s in sys.stdin.readline().split()]
angles = []
for _ in range(N):
    angles.append(int(sys.stdin.readline()))
print(angles)


div_map = defaultdict(set)
distances = []
remain_indices = [i for i in range(N)]
min_heap = []
for i in range(N):
    if i == N - 1:
        # heapq.heappush(min_heap, (360 + angles[0] - angles[-1], -1, 0))
        # div_map[-1].add(0)
        distances.append((360 + angles[0] - angles[-1], -1, 0))
    else:
        # heapq.heappush(min_heap, (angles[i + 1] - angles[i], i, i + 1))
        # div_map[i].add(i + 1)
        distances.append((angles[i + 1] - angles[i], i, i + 1))


def is_added(i1: int, i2: int) -> bool:
    a, b = min(i1, i2), max(i1, i2)
    if a not in div_map:
        return False
    return b in div_map[a]


def calc(a: int, k: int) -> float:
    return (a - 1) / (2 * M) + 0.5 + k / (360 * M)


def get_dist(i1: int, i2: int) -> int:
    a, b = min(i1, i2), max(i1, i2)
    d1 = angles[b] - angles[a]
    d2 = 360 + angles[a] - angles[b]
    return min(d1, d2)




ans = 0
for a in range(M, 0, -1):
    tmpk, i1, i2 = min_heap[0]
    print(f'k={tmpk} i1={i1} i2={i2}')
    chosed = heapq.nlargest(a, distances, key=lambda x:x[0])

    ii1 = bisect.bisect_left(remain_indices, i1)
    heapq.heappop(min_heap)
    if remain_indices[ii1] != i1 or remain_indices[(ii1 + 1) % len(remain_indices)] != i2:
        continue
    c = calc(a, tmpk)
    ans = max(ans, c)
    print(f'  ans={ans} c={c}')
    if a >= 4:
        # i0, i3 = i1 - 1, i2 + 1
        i0, i3 = remain_indices[ii1 - 1], remain_indices[ii1 + 2]
        d02 = get_dist(i0, i2)
        d23 = get_dist(i2, i3)
        min2 = min(d02, d23)
        d01 = get_dist(i0, i1)
        d13 = get_dist(i1, i3)
        min1 = min(d01, d13)
        if min2 < min1: # pick 1, drop 2
            heapq.heappush(min_heap, (d13, i1, i3))
            remain_indices.pop(ii1 + 1)
            # if not is_added(i0, i1):
            #     heapq.heappush(min_heap, (d10, i0, i1))
            # if not is_added()
        else: # pick 2, drop 1
            heapq.heappush(min_heap, (d02, i0, i2))
            remain_indices.pop(ii1)

print(ans)