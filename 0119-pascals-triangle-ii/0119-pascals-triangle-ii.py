class Solution:
    def getRow(self, row: int) -> List[int]:
        if row < 2: return [1] * (row+1)
        last = [1, 1]
        for _ in range(row-1):
            res = [1]
            for i in range(len(last)-1):
                res.append(last[i]+last[i+1])
            res.append(1)
            last = res
        return res