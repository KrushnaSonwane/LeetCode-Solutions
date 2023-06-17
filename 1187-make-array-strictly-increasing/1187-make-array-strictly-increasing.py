class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        @cache
        def dfs(i, last):
            if i >= len(arr1): return 0
            res = float("inf")
            if last < arr1[i]:
                res = min(res, dfs(i + 1, arr1[i]))
            ind = bisect.bisect_right(arr2, last)
            if ind != len(arr2):
                res = min(res, 1 + dfs(i + 1, arr2[ind]))
            return res
        res = dfs(0, -1)
        return -1 if res == float("inf") else res