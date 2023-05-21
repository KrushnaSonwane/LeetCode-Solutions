class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums1:
            if (num in nums2 or num in nums3) and num not in res:
                res.append(num)
        for num in nums3:
            if (num in nums1 or num in nums2) and num not in res:
                res.append(num)
        return res