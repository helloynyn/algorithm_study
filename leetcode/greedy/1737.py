'''
1737. Change Minimum Characters to Satisfy One of Three Conditions
'''
import string
from collections import Counter


# condition 3 두 문자열을 하나의 알파벳으로만 구성
# lenA-A에서 빈도수높은 알파벳수 + lenB-B에서 빈도수높은 알파벳수

# condition 1, 2 는 특정 문자보다 작은 알파벳으로 변경하는 수 계산

class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        cn1, cn2 = [0] * 26, [0] * 26
        for c in a: cn1[ord(c) - 97] += 1
        for c in b: cn2[ord(c) - 97] += 1

        ans = len(a) + len(b) - max(x + y for x, y in zip(cn1, cn2))  # condition 3
        for i in range(1, 26):  # note that letters can't be smaller than 'a' or bigger than 'z'
            ans = min(ans, sum(cn1[:i]) + sum(cn2[i:]), sum(cn1[i:]) + sum(cn2[:i]))
        return ans

## https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/discuss/1032044/Python-Loop-through-separating-letter