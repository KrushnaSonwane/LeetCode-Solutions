class Solution:
    def balancedString(self, s: str) -> int:

        def check(k, n):
            hashT = Counter(s)
            for i in range(k-1):
                hashT[s[i]] -= 1
            for i in range(k-1, len(s)):
                hashT[s[i]] -= 1
                if max(hashT.values()) <= n: 
                    return 1
                hashT[s[i-(k-1)]] += 1
            return 0    

        n = len(s) // 4
        l, r, res = 1, len(s), inf
        
        A = Counter(s)
        for ch in A:
            if A[ch] != n: break
        else: return 0

        while r >= l:
            mid = (r + l) // 2
            if check(mid, n):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res