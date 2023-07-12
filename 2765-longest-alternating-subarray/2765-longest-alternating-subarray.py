class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        res = float("-inf")
        n = len(nums)
        for i in range(n):
            last = nums[i]
            flag = False
            for j in range(i+1, n):
                if not flag:
                    if nums[j] - last != 1: break
                else:
                    if nums[j] - last != -1: break
                flag = not flag
                last = nums[j]
                res = max(res, j - i + 1)
        return -1 if res == float("-inf") else res