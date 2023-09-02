class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        hashT = Counter(s)
        A = [hashT[ch] for ch in hashT]
        A.sort(reverse = True)
        if k > len(A): return 0
        hashT = set()
        for i in range(k):
            hashT.add(A[i])
        min_ = min(hashT)
        mod = 10**9+7
        
        @lru_cache
        def dfs(i, k):
            if k == 0: return 1
            if i == len(A): return 0
            if A[i] < min_: return 0
            if A[i] > min_:
                res = A[i] * dfs(i+1, k-1)
            else:
                res = (A[i] * dfs(i+1, k-1)) + dfs(i+1, k)
            res %= mod
            return res
        return dfs(0, k)