class Solution:
    def mostBooked(self, n: int, A: List[List[int]]) -> int:
        Q, has, hashT = [], [], defaultdict(int)

        for i in range(n):
            heappush(has, i)
        max_ = 0

        for l, r in sorted(A):
            while Q and Q[0][0] <= l or not has:
                last, room = heappop(Q)
                hashT[room] += 1
                max_ = max(last, max_)
                heappush(has, room)
            heappush(Q, [max(max_+ (r-l), r), heappop(has)])

        while Q: hashT[heappop(Q)[1]] += 1

        res, count = inf, 0
        for num in hashT:
            if hashT[num] > count:
                count = hashT[num]
                res = num
            elif hashT[num] == count:
                res = min(res, num)
        return res