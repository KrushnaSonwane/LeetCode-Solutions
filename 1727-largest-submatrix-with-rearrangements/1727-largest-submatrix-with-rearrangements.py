class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        hashT = defaultdict(list)
        for j in range(len(matrix[0])):
            count = 0
            for i in range(len(matrix)):
                count += 1 if matrix[i][j] else -count
                hashT[i].append(count)
        res = 0
        for row in hashT:
            A = sorted(hashT[row])[::-1]
            min_, length = inf, 0
            for num in A:
                length += 1
                min_ = min(min_, num)
                res = max(res, min_ * length)
        return res