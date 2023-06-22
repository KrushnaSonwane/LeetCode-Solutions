from sortedcontainers import SortedList
class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        res = [float("inf")] * n
        nums = nums + nums
        ans = float("inf")
        for i in range(n):
            sum_ = 0
            for j in range(n):
                res[j] = min(res[j], nums[i + j])
                sum_ += res[j]
            ans = min(ans, sum_ + (x * i))
        return ans