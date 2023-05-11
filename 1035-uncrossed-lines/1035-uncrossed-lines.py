class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        dp = [[-1 for _ in nums2] for _ in nums1]
        def dfs(i, j):
            if i == len(nums1) or j == len(nums2): return 0
            if dp[i][j] != -1: return dp[i][j]
            if nums1[i] == nums2[j]:
                dp[i][j] = 1 + dfs(i + 1, j + 1)
            else:
                dp[i][j] = max(dfs(i + 1, j), dfs(i, j + 1))
            return dp[i][j]
        return dfs(0, 0)