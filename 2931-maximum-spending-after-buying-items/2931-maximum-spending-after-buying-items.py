class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        Q, res, day = [], 0, 1
        for i in range(len(values)):
            heappush(Q, (values[i][-1], i, len(values[i])-1))
        while Q:
            val, i, j = heappop(Q)
            if j-1 >= 0: heappush(Q, (values[i][j-1], i, j-1))
            res += val * day
            day += 1
        return res