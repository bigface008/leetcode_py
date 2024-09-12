# https://leetcode.com/problems/wildcard-matching/description/
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        NS = len(s)
        j = 0
        p_groups = p.split('*')
        for p_group in p_groups:
            i = 0
            first_ch_i = -1
            while i < len(p_group):
                if p_group[i] == '?':
                    i += 1
                else:
                    first_ch_i = i
                    break
            if first_ch_i == -1:
                j += len(p_group)
                if j >= NS:
                    return False
                continue
            match_j = -1
            while j < NS:
                if s[j] == p_group[first_ch_i]:
                    match_j = j
                    break
                j += 1
            if match_j == -1:
                return False
            j2 = match_j + 1
            i2 = first_ch_i + 1
            while i2 < len(p_group) and j2 < len(match_j):
                if p_group[i2] != s[j2] and p_groups[i2]:

        return True
