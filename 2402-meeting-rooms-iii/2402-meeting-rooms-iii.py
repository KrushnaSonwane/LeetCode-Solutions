class Solution:
    def mostBooked(self, n: int, M: List[List[int]]) -> int:
        Q = [i for i in range(n)]
        A, stack = Counter(), []
        for l, r in sorted(M):
            while stack and stack[0][0] <= l:
                _, room = heappop(stack)
                heappush(Q, room)
            if Q:
                room = heappop(Q)
                A[room] += 1
                heappush(stack, [r, room])
            else:
                end, room = heappop(stack)
                A[room] += 1
                heappush(stack, [max(l, end) + (r - l), room])
        max_ = max(A.values())
        res = inf
        for num in A:
            if max_ == A[num]: res = min(res, num)
        return res