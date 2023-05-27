class Solution(object):
    def maxStrength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) ==1: return nums[0]
        negNums, res = [], 0
        for num in nums:
            if num < 0: negNums.append(num)
            elif num > 0: 
                if res == 0: res = num
                else: res *= num
        negNums.sort()
        if len(negNums) % 2: negNums.pop()
        while negNums:
            ele = negNums.pop()
            if res == 0: res = ele
            else: res *= ele
        return res