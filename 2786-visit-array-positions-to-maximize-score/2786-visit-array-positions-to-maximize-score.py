class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        @cache
        def dfs(i, isEven):
            if i == len(nums): return 0
            res = dfs(i+1, isEven)
            if nums[i]%2:
                if isEven:
                    res = max(res, nums[i]-k+dfs(i+1, False))
                else:
                    res = max(res, nums[i]+dfs(i+1, False))
            else:
                if isEven:
                    res = max(res, nums[i]+dfs(i+1, True))
                else:
                    res = max(res, nums[i]-k+dfs(i+1, True))
            return res
        return dfs(0, nums[0]%2==0)
                    