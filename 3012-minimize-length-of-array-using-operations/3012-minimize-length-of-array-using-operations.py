class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        hashT = Counter(nums)
        A = [[num, hashT[num]] for num in hashT]
        A.sort()
        if len(A) == 1:
            return (A[0][1] + 1) // 2
        min_ = inf
        for num, _ in A:
            if num % A[0][0] != 0:
                min_ = min(min_, num % A[0][0])
        if min_ < A[0][0]: return 1
        return (A[0][1] + 1) // 2