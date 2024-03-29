class Solution:
    def canEat(self, A: List[int], Q: List[List[int]]) -> List[bool]:
        for i in range(1, len(A)): A[i]+=A[i-1]
        res = []
        for ty, day, cap in Q:
            prev=0
            if ty >= 1: prev=A[ty-1]
            sum_ = A[ty]
            res.append(not(sum_ <= day or prev >= cap*(day+1)))
        return res