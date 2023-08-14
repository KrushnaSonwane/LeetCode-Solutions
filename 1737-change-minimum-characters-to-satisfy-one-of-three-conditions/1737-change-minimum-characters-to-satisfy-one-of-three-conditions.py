class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        A, B = Counter(a), Counter(b)
        def solve(A, B):
            ans = inf
            for i in range(98, 123):
                ch = chr(i)
                res = sum(A[aa] for aa in A if ch > aa)
                res += sum(B[bb] for bb in B if bb >= ch)
                ans = min(ans, res)
            unq = (len(a) - max(A.values())) + (len(b) - max(B.values()))
            return min(ans, unq)
        return min(solve(A, B), solve(B, A))