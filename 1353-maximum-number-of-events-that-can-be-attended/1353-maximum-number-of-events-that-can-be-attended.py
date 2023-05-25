class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        res, days = 0, max(max(l, r) for l, r in events)
        events.sort()
        queue = []
        ptr, n = 0, len(events)
        for d in range(1, days + 1):
            while n > ptr and events[ptr][0] == d:
                heapq.heappush(queue, events[ptr][1])
                ptr += 1
            while queue and queue[0] < d:
                heapq.heappop(queue)
            if queue:
                res += 1
                heapq.heappop(queue)
        return res