class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for val in asteroids:
            if val > 0: stack.append(val)
            else:
                if not stack:
                    stack.append(val)
                elif stack and stack[-1] < 0:
                    stack.append(val)
                else:
                    while stack and stack[-1] > 0 and stack[-1] < abs(val):
                        stack.pop()
                    if not stack:
                        stack.append(val)
                    elif stack and stack[-1] > 0 and stack[-1] == abs(val):
                        stack.pop()
                    elif stack and stack[-1] > abs(val): continue
                    else: stack.append(val)
        return stack