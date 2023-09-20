class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if sum(nums) < x: return -1
        lSum, i = 0, 0
        while i < len(nums) and lSum + nums[i] <= x:
            lSum += nums[i]
            i += 1
        res, j = i if lSum == x else inf, -1
        i -= 1
        rSum = 0
        for j in range(len(nums)-1, -1, -1):
            rSum += nums[j]
            while i >= 0 and lSum + rSum > x:
                lSum -= nums[i]
                i -= 1
            if lSum + rSum == x:
                res = min(res, len(nums)-j + i + 1)
        return -1 if res == inf else res