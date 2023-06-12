class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        queue = [0]
        for l, r in sorted(intervals):
            val = heapq.heappop(queue)
            if val >= l: heapq.heappush(queue, r)
            else: val = r
            heapq.heappush(queue, val)
        return len(queue)