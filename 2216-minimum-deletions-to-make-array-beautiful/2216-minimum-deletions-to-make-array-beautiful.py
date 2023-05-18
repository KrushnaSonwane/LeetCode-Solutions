class Solution(object):
    def minDeletion(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n, ptr1, ptr2 = len(nums), 0, 1
        res = 0
        while ptr2 < n and ptr1 < n:
            if nums[ptr1] == nums[ptr2]:
                ptr1 += 1
                ptr2 += 1
                res += 1
            else:
                ptr1 += 2
                ptr2 += 2
        return res + (n - res) % 2