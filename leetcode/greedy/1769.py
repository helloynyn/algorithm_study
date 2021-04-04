'''
1769. Minimum Number of Operations to Move All Balls to Each Box
'''


class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        n=len(boxes)
        ans=[0]*len(boxes)
        for i in range(n):
            for j in range(n):
                if i!=j and boxes[j]=='1':
                    ans[i]+=abs(i-j)
        return ans
