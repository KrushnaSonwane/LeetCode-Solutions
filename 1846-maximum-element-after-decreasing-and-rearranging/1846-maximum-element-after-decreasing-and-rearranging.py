class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, A: List[int]) -> int:
        A.sort()
        last = 1
        for num in A[1:]:
            last = min(last + 1, num)
        return last