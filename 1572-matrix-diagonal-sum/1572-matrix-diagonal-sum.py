class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        sum_, n = 0, len(mat)
        for i in range(len(mat)):
            sum_ += mat[i][i]
            mat[i][i] = 0
            sum_ += mat[i][n - i - 1]
        return sum_