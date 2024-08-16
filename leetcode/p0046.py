from typing import List, Set


# https://leetcode.com/problems/permutations/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        st = set(nums)
        ans = []
        path = [0 for _ in range(len(nums))]

        def dfs(i: int, st: Set[int]):
            if i == len(nums):
                ans.append(path.copy())
                return
            for j in st:
                path[i] = j
                dfs(i + 1, st - {j})

        dfs(0, st)
        return ans


if __name__ == '__main__':
    st = {'abs', 'tbs', 'rob', 'ted'}
    st.discard('dude')
    print(st)
    st.discard('tbs')
    print(st)
    print(st - {'rob'})
    print(st)
    print(st.intersection({'ted', '123'}))

    d = {'123': 123, '234': 234}
