class Solution:
    def maxSlidingWindow(self, A: List[int], k: int) -> List[int]:
        Q, res = [], []
        for i, num in enumerate(A):
            while Q and A[Q[-1]] <= num:
                Q.pop()
            Q.append(i)
            if i-k == Q[0]: 
                Q.pop(0)
            if i+1 >= k:
                res.append(A[Q[0]])
        return res