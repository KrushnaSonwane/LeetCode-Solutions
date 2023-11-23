class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for ll, rr in zip(l, r):
            A = sorted(nums[ll: rr+1])
            for i in range(2, len(A)):
                if A[i] - A[i-1] != A[1] - A[0]:
                    res.append(False)
                    break
            else:
                res.append(True)
        return res