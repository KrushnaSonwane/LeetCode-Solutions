class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        times = [[s, e, i] for i, (s, e) in enumerate(times)]
        times.sort()
        t = max(max(s, e) for s, e, _ in times)
        n = len(times)
        queue = [i for i in range(n)]
        heapq.heapify(queue)
        rem = []
        ptr = 0
        for currTime in range(1, t + 1):
            while rem and rem[0][0] == currTime:
                _, chair = heappop(rem)
                heappush(queue, chair)
            start, end, ind = times[ptr]
            if ind == targetFriend and start == currTime: return heappop(queue)
            if start == currTime:
                heappush(rem, [end, heappop(queue)])
                ptr += 1
        return -1