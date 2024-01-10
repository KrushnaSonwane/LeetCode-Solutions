class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        hashT, res = {(a, b) for a, b in obstacles}, 0
        A = {'N': [0, 1], 'E': [1, 0], 'S': [0, -1], 'W': [-1, 0]}
        left = {'N': 'W', 'E': 'N', 'S': 'E', 'W': 'S'}
        right = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
        D, X, Y = 'N', 0, 0
        for c in commands:
            if c == -2:
                D = left[D]
            elif c == -1:
                D = right[D]
            else:
                for _ in range(c):
                    x = X + A[D][0]
                    y = Y + A[D][1]
                    if (x, y) in hashT: continue
                    X, Y = x, y
                    res = max(res, abs(X)**2+abs(Y)**2)
        return res