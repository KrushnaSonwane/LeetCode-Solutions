class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def dfs(i, j, alice):
            if i > j: return 0
            if alice:
                res = max(nums[j]+dfs(i,j-1,False), nums[i]+dfs(i+1,j,False))
            else:
                res = min(-nums[j]+dfs(i,j-1,True), -nums[i]+dfs(i+1,j,True))
            return res
        return dfs(0,len(nums)-1,True) >= 0