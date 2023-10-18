class Solution:
    def minHeightShelves(self, books: List[List[int]], width: int) -> int:
        @cache
        def dfs(i):
            if i == len(books): return 0
            w, h = 0, 0
            res = inf
            for j in range(i, len(books)):
                w += books[j][0]
                if w > width: break
                h = max(h, books[j][1])
                res = min(res, dfs(j+1) + h)
            return res
        return dfs(0)