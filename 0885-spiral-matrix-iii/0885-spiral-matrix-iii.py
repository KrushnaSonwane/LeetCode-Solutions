class Solution:
    def spiralMatrixIII(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        res, size = [[r, c]], 1
        while len(res) != m * n:
            for _ in range(size):
                c += 1
                if 0 <= r < m and 0 <= c < n:
                    res.append([r, c])
            for _ in range(size):
                r += 1
                if 0 <= r < m and 0 <= c < n:
                    res.append([r, c])
            size += 1
            for _ in range(size):
                c -= 1
                if 0 <= r < m and 0 <= c < n:
                    res.append([r, c])
            for _ in range(size):
                r -= 1
                if 0 <= r < m and 0 <= c < n:
                    res.append([r, c])
            size += 1
        return res