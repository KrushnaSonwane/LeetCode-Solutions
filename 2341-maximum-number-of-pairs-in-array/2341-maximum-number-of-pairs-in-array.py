class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashT = collections.Counter(nums)
        pairs = sum(hashT[num] // 2 for num in hashT)
        return [pairs, len(nums) - pairs * 2]