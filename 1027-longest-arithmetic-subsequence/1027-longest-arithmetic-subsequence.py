class Solution(object):
    def longestArithSeqLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3: return n
        dp = {}
        for i in range(n):
            for j in range(i+1, n):
                d = nums[i] - nums[j]
                if (d, i) in dp:
                    dp[(d, j)] = dp[(d, i)] + 1
                else:
                    dp[(d, j)] = 2
        return max(dp.values())