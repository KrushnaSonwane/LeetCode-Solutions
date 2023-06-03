class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, sum_):
            if i == len(nums): return sum_
            return dfs(i + 1, sum_) + dfs(i + 1, sum_ ^ nums[i])
        return dfs(0, 0)