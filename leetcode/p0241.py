from typing import List


# https://leetcode.com/problems/different-ways-to-add-parentheses/description/?envType=daily-question&envId=2024-09-19
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ans_st = set()

        def do_op(op: str, a: int, b: int) -> int:
            if op == '+':
                return a + b
            elif op == '-':
                return a - b
            else:
                return a * b

        def dfs(exp: str) -> List[int]:
            if not exp:
                return []
            has_op = False
            ans = []
            for i, ch in enumerate(exp):
                if not ch.isnumeric():
                    has_op = True
                    ans1 = dfs(exp[:i])
                    ans2 = dfs(exp[i + 1:])
                    for a1 in ans1:
                        for a2 in ans2:
                            ans.append(do_op(ch, a1, a2))
            if not has_op:
                return [int(exp)]
            return ans

        return dfs(expression)

        # split
        # nums = []
        # ops = []
        # for i, ch in enumerate(expression):
        #     if ch.isnumeric():
        #         if i < len(expression) and expression[i + 1].isnumeric():
        #             n = int(expression[i:i + 2])
        #         else:
        #             n = int(ch)
        #         nums.append(n)
        #     else:
        #         ops.append(ch)

        # return list(ans_st)
