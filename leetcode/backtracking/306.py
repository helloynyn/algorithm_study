class Solution:
    def __init__(self):
        self.ans=False

    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(curStr, numList): # curStr에서 numList에 들어갈 수를 찾는 함수
            if self.ans: return
            if not curStr and len(numList)>=3:
                self.ans=True
                return

            for x in range(1, len(curStr)+1): # 틀린부분) 끝나는 범위를 헷갈렸음
                if x>=2 and curStr[0]=='0': return # no leading zero
                tmpNum=int(curStr[:x])
                if numList and len(numList)>=2:
                    if tmpNum==numList[-1]+numList[-2]:
                        dfs(curStr[x:], numList + [tmpNum])
                    elif tmpNum<numList[-1]+numList[-2]:
                        continue
                    else: # backtracking
                        return
                else:
                    dfs(curStr[x:], numList+[tmpNum])

        dfs(num, [])
        return self.ans

s=Solution()
print(s.isAdditiveNumber("199100199"))

# 배운점
# argument 에 list.append 사용하니 None이 전달되는 문제있었음.
# append는 list 변수에 적용되고, 리턴값은 None 이기 때문!
# https://stackoverflow.com/questions/32160653/python-2-7-using-list-append-in-function-arguments

