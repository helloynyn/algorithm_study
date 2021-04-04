'''
1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
'''


class Solution:
    def minPartitions(self, n: str) -> int:
        return max(set(map(int, set(n))))
