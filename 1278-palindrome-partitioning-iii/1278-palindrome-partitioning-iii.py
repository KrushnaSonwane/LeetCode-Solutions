class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        @cache
        def dfs(i, k):
            if len(s[i:]) == k: return 0
            if k == 1:
                count = 0
                l, r = i, len(s) - 1
                while r > l:
                    count += s[l] != s[r]
                    l += 1
                    r -= 1
                return count
            res = float("inf")
            for j in range(i, len(s) - (k - 1)):
                l, r = i, j
                count = 0
                while r > l:
                    count += s[l] != s[r]
                    l += 1
                    r -= 1
                res = min(res, count + dfs(j + 1, k - 1))
            return res
        return dfs(0, k)