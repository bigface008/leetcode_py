# 给定一个正整数数组和k，求其所有子数组中进行or操作后第k大的结果
# 比如[2,5,7]
# 其子数组的or操作结果从大到小排序
# [2,5,7] 7
# [5,7] 7
# [2,5] 7
# [2,7] 7
# 当k为3，结果就是7
# 解法有两步，先假设直接有个函数 getNumber(start, end) 直接计算出 start 和 end 中的所有数的or结果
# 这个函数本身需要用 2D prefix sum 来做
import heapq
from typing import List


def getNumber(start: int, end: int) -> int:
    return 0


# 主要思路是 首先最大的一定是[2,5,7]，即整个数组
# 那么接下来会如何变小呢？
# 一定是去掉左边或者右边的数！
# 即有
# k=1 max([2,5,7])
# k=2 max([2,5],[5,7])
# k=3 max([2,5],[5],[7])
def solution(nums: List[int], k: int) -> int:
    N = len(nums)
    hp = [(-getNumber(0, N - 1), 0, N - 1)]
    st = set()
    st.add((0, N - 1))
    i = 0
    while i < k:
        i += 1
        val, start, end = hp[0]
        if start == end:
            continue
        if (start + 1, end) not in st:
            heapq.heappush(hp, (-getNumber(start + 1, end), start + 1, end))
            st.add((start + 1, end))
        if (start, end - 1) not in st:
            heapq.heappush(hp, (-getNumber(start, end - 1), start, end - 1))
            st.add((start, end - 1))
    return -hp[0][0]