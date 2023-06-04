class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        cols, rows = set(), set()
        res = 0
        for ty, index, val in queries[::-1]:
            if ty:
                if index not in cols:
                    cols.add(index)
                    res += val * n
                    res -= val * len(rows)
            else:
                if index not in rows:
                    rows.add(index)
                    res += val * n
                    res -= val * len(cols)
        return res