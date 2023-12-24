class Solution:
    def minimumCost(self, source: str, target: str, O: List[str], C: List[str], CC: List[int]) -> int:
        A = [[inf for _ in range(26)] for _ in range(26)]
        for i in range(26):
            A[i][i] = 0
        res = 0
        for a, b, c in zip(O, C, CC):
            a, b = ord(a)-97, ord(b)-97
            A[a][b] = min(A[a][b], c)
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    A[i][j] = min(A[i][j], A[i][k] + A[k][j])
        for a, b in zip(source, target):
            a, b = ord(a)-97, ord(b)-97
            if A[a][b] == inf: return -1
            res += A[a][b]
        return res