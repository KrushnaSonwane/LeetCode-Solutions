class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        arr = [val for val, _, _ in events]
        @cache
        def dfs(i, k):
            if k == 0 or i >= len(arr): return 0
            notTake = dfs(i + 1, k)
            ind = bisect.bisect_left(arr, events[i][1] + 1)
            take = dfs(ind, k - 1) + events[i][2]
            return max(take, notTake)
        return dfs(0, k)