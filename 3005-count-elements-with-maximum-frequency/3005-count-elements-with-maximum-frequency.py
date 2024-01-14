class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        A = Counter(nums)
        max_ = max(A.values())
        res = 0
        for num in A:
            if A[num] == max_:
                res += max_
        return res