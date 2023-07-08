class Solution:
    def eatenApples(self, A: List[int], D: List[int]) -> int:
        max_ = max(i+D[i] for i in range(len(A)))
        res, Q = 0, []
        for d in range(max_):
            if d < len(A) and A[d]: heappush(Q, [d+D[d], A[d]])
            while Q and Q[0][0] <= d: heappop(Q)
            if Q:
                dy, count = heappop(Q)
                res += 1
                if count >= 2: heappush(Q, [dy, count-1])
        return res