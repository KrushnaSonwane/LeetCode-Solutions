class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res, i, j, max_, A = 0, 0, 0, max(nums), defaultdict(int)
        while j < len(nums):
            A[nums[j]] += 1
            while A[max_] == k:
                res += len(nums)-j
                A[nums[i]] -= 1
                i += 1
            j += 1
        return res