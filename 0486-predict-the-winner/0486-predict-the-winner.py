class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def dfs(i, j, alice):
            if i > j: return 0
            if alice: return max(nums[j]+dfs(i,j-1,False), nums[i]+dfs(i+1,j,False))
            return min(-nums[j]+dfs(i,j-1,True), -nums[i]+dfs(i+1,j,True))
        return dfs(0,len(nums)-1,True) > -1