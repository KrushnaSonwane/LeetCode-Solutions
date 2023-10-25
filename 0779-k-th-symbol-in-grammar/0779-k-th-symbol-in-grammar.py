class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        A, temp = [], k
        for i in range(n-1, 0, -1):
            A.append(ceil(k / 2))
            k = ceil(k/2)
        def check(last, index):
            if last == index % 2 == 0: 
                return 1
            if last and index % 2 == 0:
                return 0
            return last
        A, res = A[::-1] + [temp], 0
        for i in A[1:]:
            res = check(res, i)
        return res