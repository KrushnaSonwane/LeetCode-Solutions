class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        def dfs(num):
            if num in visit: return 0
            visit.add(num)
            return dfs(nums[num]) + 1
        visit, res = set(), 0
        for num in nums:
            res = max(res, dfs(num))
        return res