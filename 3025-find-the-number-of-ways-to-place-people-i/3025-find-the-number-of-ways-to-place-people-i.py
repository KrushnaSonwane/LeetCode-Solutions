class Solution:
    def numberOfPairs(self, A: List[List[int]]) -> int:
        res = 0
        for i in range(len(A)):
            for j in range(len(A)):
                if i == j: continue
                a, b = A[i]
                x, y = A[j]
                if a <= x and b >= y:
                    for k in range(len(A)):
                        if k == i or j == k: continue
                        p, q = A[k]
                        if a <= p <= x and y <= q <= b:
                            break
                    else:
                        res += 1
        return res