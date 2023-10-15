class Solution:
    def constructProductMatrix(self, A: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                res.append([A[i][j], i, j])
        prod = res[0][0]
        AA = [1]
        for i in range(1, len(res)):
            AA.append(prod)
            prod *= res[i][0]
            prod %= 12345
        prod = res[-1][0]
        BB = [1]
        for i in range(len(res)-2, -1, -1):
            BB.append(prod)
            prod *= res[i][0]
            prod %= 12345
        BB = BB[::-1]
        ans = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
        for i in range(len(res)):
            _, a, b = res[i]
            ans[a][b] = (AA[i] * BB[i]) % 12345
        return ans