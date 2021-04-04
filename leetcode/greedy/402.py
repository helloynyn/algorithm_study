'''
class Solution:
    def minPartitions(self, n: str) -> int:
        return max(set(map(int, set(n))))
'''


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ## approach : stack
        ## 1234, k=2 -> when numbers are in increasing order we need to delete last digits
        ## 4321, k=2 -> when numbers are in decreasing order we need to delete first digits
        ## so, we need to preserve increasing sequence and remove decreasing sequence
        ## logic
        # 1. First think in terms of stack
        # 2. push num into stack IF  num it is greater than top of stack
        # 3. else pop all elemnts less than num

        stack = []
        for n in num:
            while (stack and int(stack[-1]) > int(n) and k):
                # 스택이 비어있지 않고
                # top of stack 보다 현재 바라보는 n 값이 클때
                # 제거할 숫자가 k 개 남아있을때
                # 스택 탑 제거
                stack.pop()
                k -= 1
            # 아니면 스택에 넣는다.
            stack.append(str(n))

        # if no elements are removed, pop last elements, (increasing order)
        while (k):
            stack.pop()
            k -= 1

        # removing leading zeros
        i = 0
        while (i < len(stack) and stack[i] == '0'):
            # 스택 원소 안에서
            # 처음으로 0이 아닌 자릿수 찾음
            i += 1

        return ''.join(stack[i:]) if len(stack[i:]) > 0 else "0"
