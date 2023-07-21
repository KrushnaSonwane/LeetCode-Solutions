class Solution:
    def findNumberOfLIS(self, A: List[int]) -> int:
        res, size = [1 for _ in A], [1 for _ in A]
        for i in range(len(A)):
            for j in range(i):
                if A[i] > A[j]:
                    if size[j]+1 > size[i]:
                        size[i] = size[j]+1
                        res[i] = 0
                    if size[j]+1 == size[i]:
                        res[i] += res[j]
        return sum(res[i] for i in range(len(A)) if size[i]==max(size))