class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        A = sorted([ceil(d / s) for d, s in zip(dist, speed)])
        for i in range(len(A)):
            if A[0] <= i: break
            A.pop(0)
        return len(dist) - len(A) 