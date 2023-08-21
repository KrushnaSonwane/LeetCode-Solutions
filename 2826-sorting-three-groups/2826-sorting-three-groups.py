class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        @cache
        def dfs(i, last):
            if i == len(nums): return 0
            res = inf
            for j in range(last, 4):
                res = min(res, dfs(i+1, j) + int(nums[i] != j))
            return res
        return dfs(0, 1)