class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = [0 for _ in range(n)], [0 for _ in range(n)]
        stack = [-1]
        for i, num in enumerate(nums):
            while len(stack) > 1 and nums[stack[-1]] >= num:
                stack.pop()
            left[i] = i - stack[-1]
            stack.append(i)
        stack = [n]
        
        for i in range(n-1, -1, -1):
            while len(stack) > 1 and nums[stack[-1]] > nums[i]:
                stack.pop()
            right[i] = stack[-1] - i
            stack.append(i)
            
        res, MOD = 0, 10**9+7
        for i, num in enumerate(nums):
            res = (res + (left[i] * right[i]) * num) % MOD
        return res