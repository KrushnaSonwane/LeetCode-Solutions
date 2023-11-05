class Solution:
    def countCollisions(self, directions: str) -> int:
        stack, res = [], 0
        r, s = 0, 0
        for d in directions:
            if d == 'R':
                r, s = r + 1, 0
            elif d == 'S':
                if r:
                    res += r
                r, s = 0, 1
            else:
                if r:
                    res += r + 1
                    s, r = 1, 0
                elif s:
                    res += 1
        return res