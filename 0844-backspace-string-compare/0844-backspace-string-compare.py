class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def solve(a):
            stack = []
            for char in a:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
            return stack
        return solve(s) == solve(t)