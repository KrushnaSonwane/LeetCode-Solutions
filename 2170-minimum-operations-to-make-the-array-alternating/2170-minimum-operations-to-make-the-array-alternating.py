class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums)==1: return 0
        if len(nums)==2: return 1 if nums[0]==nums[1] else 0
        A, B = defaultdict(int), defaultdict(int)
        a, b = 0, 0
        for i, num in enumerate(nums):
            if i % 2:
                A[num] += 1
                a += 1
            else:
                B[num] += 1
                b += 1
        A, B = [[A[aa], aa] for aa in A], [[B[bb], bb] for bb in B]
        A.sort(reverse = True)
        B.sort(reverse = True)
        res = len(nums)
        for x, y in A:
            if B[0][1] != y:
                res = min(res, a - x + b - B[0][0])
            else:
                res = min(res, b + a -x)
        for x, y in B:
            if B[0][1] != y:
                res = min(res, b - x + a - A[0][0])
            else:
                res = min(res, a + b-x)
        return res