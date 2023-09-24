class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        res = [float(poured)]
        if query_row == 0:
            return min(res[0], 1.000)
        for i in range(query_row):
            curr = [0.00 for _ in range(len(res)+1)]
            for j in range(len(res)):
                remain = res.pop(0) - 1
                if remain > 0:
                    curr[j] += remain / 2.00
                    curr[j+1] += remain / 2.00
            res = curr
        return min(1.00, res[query_glass]) 