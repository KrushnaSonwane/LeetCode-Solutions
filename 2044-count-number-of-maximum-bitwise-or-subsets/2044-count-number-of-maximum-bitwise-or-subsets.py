class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans, res = [float("-inf")], [0]
        def dfs(i, xor):
            if i == len(nums):
                if ans[0] < xor: ans[0], res[0] = xor, 1
                elif ans[0] == xor: res[0] += 1
                return
            dfs(i + 1, xor)
            dfs(i + 1, xor | nums[i])
        dfs(0, 0)
        return res[0]