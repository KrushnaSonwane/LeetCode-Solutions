class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)
        for i in range(n):
            nums = set()
            nums2  = set()
            for j in range(n):
                nums.add(matrix[i][j])
                nums2.add(matrix[j][i])
            if len(nums) != n or len(nums2) != n: return 0
        return 1