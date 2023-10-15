from sortedcontainers import SortedList
class Solution:
    def findIndices(self, nums: List[int], a: int, b: int) -> List[int]:
        A, j = SortedList(), 0
        for i in range(a, len(nums)):
            A.add([nums[j], j])
            j += 1
            if abs(A[-1][0] - nums[i]) >= b:
                return [A[-1][1], i]
            if abs(A[0][0] - nums[i]) >= b:
                return [A[0][1], i]
        return [-1, -1]