class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        l, r = 1, n
        res = []
        for _ in range(k//2):
            res.append(l)
            res.append(r)
            l += 1
            r -= 1
        f = k % 2
        while len(res) != n:
            if f:
                res.append(l)
                l += 1
            else:
                res.append(r)
                r -= 1
        return res