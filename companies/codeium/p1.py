# 给定一个target整数数组，你可以创建一个等长的全为1的数组
# 定义一次operation，算出当前数组的和，将数组中某个元素替换为和
# 问你可以通过多少次operation从初始数组得到target数组？
# 主要思路是从target开始，贪心得往回找！
import heapq
from typing import List

# 这里的复杂度是多少呢？
# 首先你每次循环都要进行heap操作，有logN的复杂度。
# 那么要循环多少次呢？实际就是ans，那么ans有什么bound吗？
# 首先你会想到，ans绝对不会超过最大元素MAX减小到1的次数，所以有
# ans <= MAX
# 有没有可能更小一点呢？
# 注意！每次最大值减小的最小值，是N - 1
# 因此 ans <= MAX // (N - 1)

def solution(target: List[int]):
    N = len(target)
    arr = target.copy()
    curr_sum = sum(arr)
    pq = []
    for x in arr:
        heapq.heappush(pq, -x)
    ans = 0
    while pq[0] != -1:
        x = pq[0]
        x = -x
        heapq.heappop(pq)
        new_x = x - (curr_sum - x)
        if new_x <= 0 or new_x >= x: # 注意这里的判断条件，这其实意思是说，我们每次都必须能够减小最大值，否则就是有问题的！
            return -1
        heapq.heappush(pq, -new_x)
        curr_sum -= x - new_x
    ans += 1
    return ans