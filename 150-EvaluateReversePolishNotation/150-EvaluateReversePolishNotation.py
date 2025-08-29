# Last updated: 8/29/2025, 8:31:09 AM
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack  = []
        for t in tokens:
            if t == '+':
                a,b = stack.pop(), stack.pop()
                stack.append(a+b)
            elif t == '-':
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif t == '*':
                a,b = stack.pop(), stack.pop()
                stack.append(a*b)
            elif t == '/':
                a,b = stack.pop(), stack.pop()
                stack.append(int(float(b)/a))
            else:
                stack.append(int(t))
        
        return stack[-1]