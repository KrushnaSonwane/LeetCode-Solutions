class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        l, r, res = 0, 0, inf
        hashT = defaultdict(int)
        count = 0
        while r < len(nums):
            hashT[nums[r]] += 1
            count += hashT[nums[r]] > 1
            while nums[r] - nums[l] > len(nums)-1:
                count -= hashT[nums[l]] > 1
                hashT[nums[l]] -= 1
                l += 1
            res = min(res, (len(nums) - (r - l + 1)) + count)
            r += 1
        return res