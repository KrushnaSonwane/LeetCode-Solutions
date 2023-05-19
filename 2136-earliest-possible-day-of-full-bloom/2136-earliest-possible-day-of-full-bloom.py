class Solution(object):
    def earliestFullBloom(self, plantTime, growTime):
        """
        :type plantTime: List[int]
        :type growTime: List[int]
        :rtype: int
        """
        nums = [[growTime[i], plantTime[i]] for i in range(len(plantTime))]
        nums.sort(reverse = True)
        res, plant = 0, 0
        for a, b in nums:
            plant += b
            res = max(res, plant + a)
        return res