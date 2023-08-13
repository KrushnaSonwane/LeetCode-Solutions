class Solution:
    def maxSum(self, nums: List[int]) -> int:
        res = -1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                x, y = [], []
                
                num = nums[i]
                while num:
                    x.append(num%10)
                    num //= 10
                    
                num = nums[j]
                while num:
                    y.append(num%10)
                    num //= 10
                    
                if max(x)==max(y):
                    res = max(res, nums[i]+nums[j])
                    
        return res