class Solution:
    def findIndices(self, nums: List[int], a: int, b: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(i-j) >= a and abs(nums[i] - nums[j]) >= b:
                    return [i, j]
        return [-1, -1]