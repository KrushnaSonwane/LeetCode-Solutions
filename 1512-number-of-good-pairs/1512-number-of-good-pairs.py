class Solution:
    def numIdenticalPairs(self, A: List[int]) -> int:
        A.sort()
        res, i, j = 0, 0, 0
        while len(A) > i:
            count = 0
            while j < len(A) and A[i] == A[j]:
                count += 1
                res += count - 1
                j += 1
            i = j
        return res