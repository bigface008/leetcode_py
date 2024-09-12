from typing import Optional, List
from utils import ListNode, newLinkedList, tst


# https://leetcode.com/problems/spiral-matrix-iv/description/?envType=daily-question&envId=2024-09-09
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        width, height = n, m
        r, c = 0, 0
        curr = head

        def getVal():
            nonlocal curr
            if curr:
                ans = curr.val
                curr = curr.next
                return ans
            else:
                return -1

        ans = [[0 for _ in range(n)] for _ in range(m)]
        while width > 0 and height > 0:
            print(f'start r={r} c={c} width={width} height={height}')
            for i in range(width):
                # print(f'  r={r} c={c}')
                ans[r][c + i] = getVal()
            for i in range(1, height):
                # print(f'  r={r} c={c}')
                ans[r + i][c + width - 1] = getVal()
            if height > 1:
                for i in range(1, width):
                    # print(f'  r={r} c={c}')
                    ans[r + height - 1][c + width - 1 - i] = getVal()
            if width > 1:
                for i in range(1, height - 1):
                    # print(f'  r={r} c={c}')
                    ans[r + height - 1 - i][c] = getVal()
            width -= 2
            height -= 2
            r += 1
            c += 1
        return ans


def tst2(m: int, n: int, head: List[int], expect: List[List[int]]):
    output = Solution().spiralMatrix(m, n, newLinkedList(head))
    tst(f'matrix m={m} n={n} head={head}', output, expect)


if __name__ == '__main__':
    tst2(3, 5, [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0], [[3, 0, 2, 6, 8], [5, 0, -1, -1, 1], [5, 2, 4, 9, 7]])
