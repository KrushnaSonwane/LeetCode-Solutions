class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.res = float("inf")
        arr = [0 for _ in range(k)]
        arr[0] = cookies[0]
        def dfs(i, k, arr):
            if i == len(cookies):
                self.res = min(self.res, max(arr))
                return
            if max(arr) >= self.res: return
            for j in range(k):
                arr[j] += cookies[i]
                dfs(i + 1, k, arr.copy())
                if j != k - 1:
                    arr[j] -= cookies[i]
        dfs(1, k, arr)
        return self.res