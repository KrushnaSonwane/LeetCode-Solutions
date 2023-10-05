class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        A = Counter(nums)
        res = []
        for num in A:
            if A[num] > len(nums) // 3:
                res.append(num)
        return res