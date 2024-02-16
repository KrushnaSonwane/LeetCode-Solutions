class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        res, count, A, j = [], 0, Counter(), 0
        for i, num in enumerate(nums):
            A[num] += 1
            count += A[num] == 1
            if i + 1 >= k:
                res.append(count)
                A[nums[j]] -= 1
                count -= A[nums[j]] == 0
                j += 1
        return res