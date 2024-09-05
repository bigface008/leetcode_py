from typing import List

import utils


# 原题是把一棵二叉树转换成一棵完全二叉搜索树，不过底层叶子节点是从右侧开始的。结果用bfs输出
# 为了简化，这里就直接给一个数组，输出其元素组成的反向完全二叉搜索树的bfs即可。

def solution(arr: int) -> List[int]:
    pass


def tst(arr: List[int], expect: List[int]):
    output = solution(arr)
    utils.tst(f'arr={arr}', output, expect)


if __name__ == '__main__':
    tst([1, 2, 3, 4, 5], [2, 1, 4, 3, 5])
    # tst()

