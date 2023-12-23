class Solution:
    def isPathCrossing(self, path: str) -> bool:
        A = {"N": [-1, 0], 'E': [0, 1], 'S': [1, 0], 'W': [0, -1]}
        hashT = set({(0,0)})
        x, y = 0, 0
        for ch in path:
            xx, yy = A[ch]
            x += xx
            y += yy
            if (x, y) in hashT: return True
            hashT.add((x, y))
        return False