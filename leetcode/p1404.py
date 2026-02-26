# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/?envType=daily-question&envId=2026-02-26
class Solution:
    def numSteps(self, s: str) -> int:
        digits = list(map(int, s))
        ans = 0
        while len(digits) != 1:
            if digits[-1] == 0:
                ans += 1
                digits.pop()
            else:
                i = len(digits) - 1
                ans += 1
                while i >= 0 and digits[i] == 1:
                    digits[i] = 0
                    i -= 1
                if i < 0:
                    digits.insert(0, 1)
                else:
                    digits[i] = 1
        return ans


if __name__ == "__main__":
    print(Solution().numSteps("1101"))
