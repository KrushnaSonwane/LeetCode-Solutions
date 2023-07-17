class Solution:
    def canMakePaliQueries(self, s: str, Q: List[List[int]]) -> List[bool]:
        res, A = [], []
        hashT = defaultdict(int)
        for i, ch in enumerate(s):
            hashT[ch] += 1
            A.append(hashT.copy())
        for l, r, k in Q:
            f = defaultdict(int)
            if l != 0: f = A[l-1]
            count = 0
            for ch in A[r]:
                count += (A[r][ch] - f[ch]) % 2
            if not count: res.append(True)
            else:
                if (r-l+1) % 2: count -= 1
                res.append(k >= count // 2)
        return res