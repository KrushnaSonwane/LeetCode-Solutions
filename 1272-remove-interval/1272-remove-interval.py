class Solution:
    def removeInterval(self, A: List[List[int]], B: List[int]) -> List[List[int]]:
        x, y = B
        res = []
        for l, r in sorted(A):
            if x >= r:
                res.append([l, r])
            elif l >= y:
                res.append([l, r])
            else:
                if l < x and r >= x:
                    res.append([l, x])
                if y >= l and r > y:
                    res.append([y, r])
        return res