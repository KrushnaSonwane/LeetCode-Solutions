class Solution:
    def numIdenticalPairs(self, A: List[int]) -> int:
        return sum(1 for i in range(len(A)) for j in range(i+1, len(A)) if A[i]==A[j])