class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min_, n = inf, len(matrix)
        sum_ = count = 0
        for i in range(n):
            for j in range(n):
                val = abs(matrix[i][j])
                min_ = min(val, min_)
                sum_ += val
                count += matrix[i][j] < 0
        if count % 2: return sum_ - min_ * 2
        return sum_