class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for i in num:
            while k and stack and i < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(i)
        
        if k != 0:
            stack = stack[:-k]
        
        answer = ''.join(stack).lstrip('0')
        
        return answer if answer else '0'