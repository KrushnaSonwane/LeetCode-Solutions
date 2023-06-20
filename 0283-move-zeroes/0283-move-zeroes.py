class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeros = sum(1 for val in nums if not val)
        ptr1, ptr2 = 0, 0
        while ptr2 < len(nums):
            while len(nums) > ptr1 and nums[ptr1]:
                ptr1 += 1
            if ptr2 <= ptr1:
                ptr2 = ptr1
            while len(nums) > ptr2 and not nums[ptr2]:
                ptr2 += 1
            if ptr1 < len(nums) and ptr2 < len(nums):
                nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
        for i in range(1, zeros + 1):
            nums[-i] = 0