class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        z = 0
        for i in range(1, len(nums)):
            if nums[i] == 0: z += 1
        rP = 1
        c = z
        for i in range(1, len(nums)):
            if not(z): rP *= nums[i]
            if nums[i] == 0: z -= 1
        z = c
        lP = nums[0]
        if z > 0: nums[0] = 0
        else: nums[0] = rP
        for i in range(1, len(nums)):
            temp = nums[i]
            if z and nums[i] == 0:
                z -= 1
            if z:
                    nums[i] = 0
            else:
                if nums[i] != 0:
                    rP = rP // nums[i]
                nums[i] = lP * rP
            lP *= temp
        return nums