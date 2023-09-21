class Solution:
    def maxSumRangeQuery(self, nums: List[int], R: List[List[int]]) -> int:
        A, res = [0 for _ in range(len(nums)+1)], 0
        for l, r in R:
            A[l] += 1
            A[r+1] -= 1
        for i in range(1, len(A)):
            A[i] += A[i-1]
        A.pop()
        nums.sort()
        A.sort()
        for a, num in zip(A, nums):
            res += a * num
            res %= 10**9+7
        return res