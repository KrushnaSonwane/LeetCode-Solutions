class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        A = [defaultdict(int) for _ in s]
        hashT = defaultdict(int)
        for i, ch in enumerate(s):
            hashT[ch] += 1
            A[i] = hashT.copy()
        @cache
        def dfs(i, k):
            if i == len(s): return 0
            res = dfs(i+1, k) + 1
            for j in range(i, len(s)):
                count = A[j][s[i]] - A[i][s[i]] + 1
                size = j - i + 1
                if size <= k:
                    res = min(res, dfs(j+1, k-size))
                if size - count > k: break
                rem = count
                res = min(res, dfs(j+1, k - (size-count)) + 1 + (0 if size == 1 else len(str(rem))))
            return res
        return dfs(0, k)