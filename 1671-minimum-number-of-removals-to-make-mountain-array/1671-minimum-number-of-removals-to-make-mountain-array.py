class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        dp, stack = [0 for _ in range(n)], []
        for i in range(n-1, -1, -1):
            num = nums[i]
            if not stack or stack[-1] < num:
                stack.append(num)
                j = len(stack) - 1
            else:
                j = bisect_left(stack, num)
                stack[j] = num
            dp[i] = j
        res, stack = -inf, [nums[0]]

        for i in range(1, n-1):
            num = nums[i]
            if stack[-1] < num:
                stack.append(num)
                j = len(stack)-1
            else:
                j = bisect_left(stack, num)
                stack[j] = num
            if j != 0 and dp[i] != 0:
                res = max(res, j + dp[i] + 1)
        return len(nums) - res