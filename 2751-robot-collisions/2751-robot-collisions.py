class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        pos = [[val, h, d, i] for (i, val), h, d in zip(enumerate(positions), healths, directions)]
        pos.sort()
        n = len(positions)
        res = [-1]*n
        stack = []
        for p, h, d, i in pos:
            if d == 'R':
                stack.append([h, i])
            else:
                curr = h
                if stack and stack[-1][0] == h: stack.pop(); continue
                else:
                    if stack and stack[-1][0] > h:
                        stack[-1][0] -= 1
                        curr = 0
                    else:
                        while stack and stack[-1][0] < curr:
                            stack.pop()
                            curr -= 1
                        if stack and stack[-1][0] == curr:
                            stack.pop()
                            curr = 0
                        elif stack and stack[-1][0] > curr:
                            stack[-1][0] -= 1
                            curr = 0
                    if curr:
                        res[i] = curr
        for val, i in stack:
            res[i] = val
        return [val for val in res if val != -1]