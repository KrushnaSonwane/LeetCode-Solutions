class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        if n <= 2: return []
        A, res = [[n]], []
        ss = set()
        while A:
            B = [num for num in A.pop(0)]
            if tuple(sorted(B)) in ss: continue
            ss.add(tuple(sorted(B)))
            if len(B) > 1:
                res.append(B.copy())
            t = B.pop()
            for i in range(2, t // 2+1, 1):
                if t % i == 0:
                    B.append(i)
                    B.append(t // i)
                    A.append(B.copy())
                    B.pop()
                    B.pop()
        hashT = set()
        A = []
        for num in res:
            num = tuple(sorted(num))
            if num not in hashT:
                A.append(list(num))
                hashT.add(num)
        return A