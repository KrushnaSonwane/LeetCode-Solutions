class Solution:
    def minCost(self, H: List[int], C: List[List[int]], m: int, n: int, target: int) -> int:
        @cache
        def dfs(i, last, rem):
            if i == len(H): 
                return 0 if rem == 0 else inf
            # if rem == 0: return inf
            res = inf
            if H[i] != 0:
                if last == H[i]:
                    res = dfs(i+1, last, rem)
                else:
                    res = dfs(i+1, H[i], rem-1)
            else:
                for j in range(len(C[i])):
                    if j+1 != last:
                        res = min(res, dfs(i+1, j+1, rem-1) + C[i][j])
                    else:
                        res = min(res, dfs(i+1, j+1, rem) + C[i][j])
            return res
        res = dfs(0, -1, target)
        return -1 if res == inf else res