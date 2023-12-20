class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        A, B = [0], [0]
        n, sum_ = len(nums), 0
        prod = 0
        for num in nums:
            prod += num * (n-1)
            prod -= sum_
            sum_ += num
            A.append(prod)
        A.append(0)
        sum_, prod = 0, 0
        for num in nums[::-1]:
            prod += num + sum_
            sum_ += num
            B.append(prod)
        B.append(0)
        B = B[::-1]
        res = -inf
        for i in range(1, len(A)-1):
            res = max(A[i-1]+B[i+1], res)
        return res