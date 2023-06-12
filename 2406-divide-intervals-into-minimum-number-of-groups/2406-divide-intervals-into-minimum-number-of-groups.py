class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        queue = [0]
        heapq.heapify(queue)
        for l, r in intervals:
            val = heapq.heappop(queue)
            if val >= l: heapq.heappush(queue, r)
            else: val = r
            heapq.heappush(queue, val)
        return len(queue)