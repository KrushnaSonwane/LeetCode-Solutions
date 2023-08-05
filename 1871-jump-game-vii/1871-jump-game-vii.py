class Solution:
    def canReach(self, s: str, min_: int, max_: int) -> bool:
        if s[-1]!='0': return False
        stack, n = [0], len(s)
        for i in range(n):
            while stack and i-stack[0] > max_:
                stack.pop(0)
            if not stack: return False
            if s[i]=='0' and i-stack[0] >= min_: stack.append(i)
        return stack[-1]==n-1