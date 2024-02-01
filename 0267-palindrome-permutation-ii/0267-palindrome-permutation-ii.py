class Solution:
    def generatePalindromes(self, S: str) -> List[str]:
        A, count = Counter(S), 0
        t = ''
        for ch in A:
            if A[ch] % 2:
                count += 1
                t = ch
                A[ch] -= 1
        if count >= 2: return []
        res = []
        def dfs(i, a, s, t):
            if i == len(S) // 2:
                res.append(s+t+s[::-1])
                return
            for ch in a:
                if a[ch] >= 2:
                    c = ''.join(ch for ch in s)
                    a[ch] -= 2
                    c += ch
                    dfs(i+1, a, c, t)
                    a[ch] += 2
        dfs(0, A, '', t)
        return res