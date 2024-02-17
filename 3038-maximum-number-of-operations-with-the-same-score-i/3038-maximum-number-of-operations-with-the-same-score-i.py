class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        score, res = nums.pop(0) + nums.pop(0), 1
        while len(nums) >= 2:
            sum_ = nums.pop(0) + nums.pop(0)
            if sum_ == score:
                res += 1
            else: break
        return res