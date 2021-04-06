class Solution:
    def partitionLabels(self, S: str) -> list:
        D, A, p, e = {c:i for i,c in enumerate(S)}, [], -1, 0
        print(D, A, p, e)
        for i,c in enumerate(S):
            e = max(e,D[c])
            if e == i: p, _ = i, A.append(i-p)
        return A

# class Solution:
#     def partitionLabels(self, S: str) -> list:
#
#         maxi = 0
#         initial = 0
#         result = []
#         for i in range(len(S)):
#             if S.rindex(S[i]) > maxi:
#                 maxi = S.rindex(S[i])
#
#             if i == maxi:
#                 result.append(len(S[initial:maxi + 1]))
#                 initial = i + 1
#
#         return (result)

    # class Solution:
#     def partitionLabels(self, S: str) -> list:
#
#         partitions=[]
#         idx, dst, chSet=0, 0, set()
#
#         while idx<len(S):
#             cur=S[idx]
#             chSet.add(cur)
#             dst=S.rfind(cur)
#
#             while idx<=dst:
#                 if S[idx] not in chSet:
#                     chSet.add(S[idx])
#                     dst=max(dst, S.rfind(S[idx]))
#                 idx+=1
#
#             partitions.append(idx)
#
#         ans=[(partitions[i]-partitions[i-1]) for i in range(1, len(partitions))]
#         ans.insert(0, partitions[0])
#
#         return ans

s=Solution()
param = "ababcbacadefegdehijhklij"
print(s.partitionLabels(param))



