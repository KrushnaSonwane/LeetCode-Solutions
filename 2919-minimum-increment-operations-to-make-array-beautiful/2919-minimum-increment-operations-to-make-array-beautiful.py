class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        @lru_cache(None)
        def dfs(i, a, b):
            if i == len(nums): return 0
            res = inf
            if max(a, b, nums[i]) >= k:
                res = dfs(i+1, b, nums[i])
            res = min(res, dfs(i+1, b, nums[i]) + max(0, k-a))
            res = min(res, dfs(i+1, k, nums[i]) + max(0, k-b))
            res = min(res, dfs(i+1, b, k) + max(0, k-nums[i]))
            return res
        return dfs(2, nums[0], nums[1])