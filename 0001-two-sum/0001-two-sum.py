class Solution(object):
    def twoSum(self, nums, target):
        """
        Sorting + Two Pointers
        """
        hashT = {}
        for index, num in enumerate(nums):
            if target - num in hashT:
                return [index, hashT[target - num]]
            hashT[num] = index
        nums = [[val, i] for i, val in enumerate(nums)]
        nums.sort()
        l, r = 0, len(nums) - 1
        while r > l:
            if nums[l][0] + nums[r][0] == target: return [nums[l][1], nums[r][1]]
            elif nums[l][0] + nums[r][0] > target:
                r -= 1
            else:
                l += 1
        return [-1, -1]
        