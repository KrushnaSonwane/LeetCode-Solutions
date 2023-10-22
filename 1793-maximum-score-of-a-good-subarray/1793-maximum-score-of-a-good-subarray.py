class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        res, min_ = nums[k], nums[k]
        i, j, n = k-1, k+1, 1
        while i >= 0 or j < len(nums):
            if i >= 0 and j < len(nums):
                if nums[j] > nums[i]:
                    min_ = min(min_, nums[j])
                    j += 1
                elif nums[i] > nums[j]:
                    min_ = min(min_, nums[i])
                    i -= 1
                else:
                    min_ = min(min_, nums[j])
                    i -= 1
                    j += 1
                    n += 1
            elif i >= 0:
                min_ = min(min_, nums[i])
                i -= 1
            else:
                min_ = min(min_, nums[j])
                j += 1
            n += 1
            res = max(res, n * min_)
        return res