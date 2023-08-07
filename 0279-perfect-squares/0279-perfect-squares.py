class Solution:
    def numSquares(self, n: int) -> int:
        i, A = 1, []
        while i * i <= n:
            A.append(i*i)
            i += 1
        Q, res, visit = [n], 0, {n}
        while Q:
            for _ in range(len(Q)):
                num = Q.pop(0)
                if num==0: return res
                for sq in A:
                    if sq > num: break
                    if num-sq not in visit:
                        visit.add(num-sq)
                        Q.append(num-sq)
            res += 1
        return res