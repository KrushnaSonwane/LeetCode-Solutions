class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = []
        for num in nums:
            if not LIS or LIS[-1] < num:
                LIS.append(num)
            else:
                j = bisect_right(LIS, num-1)
                LIS[j] = num
        return len(LIS)