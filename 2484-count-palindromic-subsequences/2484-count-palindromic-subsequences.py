class Solution:
    def countPalindromes(self, s: str) -> int:
        A = [defaultdict(int) for _ in s]
        for i in range(10):
            for j in range(10):
                last, count = 0, 0
                for k, ch in enumerate(s):
                    A[k][(i, j)] = last
                    if int(ch) == j:
                        last += count
                    count += int(ch) ==i
        B = [defaultdict(int) for _ in s]
        for i in range(10):
            for j in range(10):
                last, count = 0, 0
                for k in range(len(s)-1, -1, -1):
                    ch = s[k]
                    B[k][(i, j)] = last
                    if int(ch) == j:
                        last += count
                    count += int(ch) == i
        res, MOD = 0, 10**9+7
        for i in range(10):
            for j in range(10):
                for k in range(2, len(s)-2, 1):
                    res = (res + A[k][(i, j)] * B[k][(i, j)]) % MOD
        return res