# https://leetcode.cn/problems/remove-duplicate-letters/description/
from typing import List
from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        left_cnt_map = Counter(s)
        ans: List[str] = []
        in_ans = set()
        for ch in s:
            left_cnt_map[ch] -= 1
            if ch in in_ans:
                continue
            while ans and ch < ans[-1] and left_cnt_map[ans[-1]]:
                in_ans.remove(ans.pop())
            ans.append(ch)
            in_ans.add(ch)
        return "".join(ans)


if __name__ == "__main__":
    print(Solution().removeDuplicateLetters("cbacdcbc"))