class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        newArr = [val for val, _, _ in events]
        @cache
        def dfs(i, t):
            if t == 2: return 0
            if i >= len(events): return 0
            return max(dfs(i + 1, t), events[i][2] + dfs(bisect.bisect_left(newArr, events[i][1] + 1), t + 1))
        return dfs(0, 0)