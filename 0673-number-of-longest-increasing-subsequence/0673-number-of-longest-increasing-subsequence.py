class Solution:
    def findNumberOfLIS(self, A: List[int]) -> int:
        count, size = [1 for _ in A], [1 for _ in A]
        for i in range(len(A)):
            for j in range(i):
                if A[i] > A[j]:
                    if size[j]+1 > size[i]:
                        size[i] = size[j]+1
                        count[i] = 0
                    if size[j]+1 == size[i]:
                        count[i] += count[j]
        max_ = max(size)
        return sum(count[i] for i in range(len(A)) if size[i]==max_)