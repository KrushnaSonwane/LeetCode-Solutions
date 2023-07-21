class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        A = []
        for num in nums:
            if not A or A[-1] < num:
                A.append(num)
            else:
                i = bisect.bisect_left(A, num)
                A[i] = num
        return len(A)