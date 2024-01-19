class Solution:
    def minimizeResult(self, ex: str) -> str:
        def getList(s):
            A = []
            for i in range(1, len(s)):
                a, b = int(s[:i]), int(s[i:])
                A.append([a, b])
            return A
        i = ex.index('+')
        a, b = ex[:i], ex[i+1:]
        A, B = getList(a), getList(b)
        min_, res = int(a) + int(b), '(' + a + '+' + b + ')'
        for x, y in A:
            sum_ = x * (y + int(b))
            if min_ > sum_:
                res, min_ = str(x) + '(' + str(y) + '+' + b + ')', sum_
        for x, y in B:
            sum_ = (int(a) + x) * y
            if min_ > sum_:
                min_, res = sum_, '(' + a + '+' + str(x) + ')' + str(y)
        for a, b in A:
            for x, y in B:
                sum_ = a * (b + x) * y
                if sum_ < min_:
                    min_, res = sum_, str(a) + '(' + str(b) + '+' + str(x) + ')' + str(y)
        return res