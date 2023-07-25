class Solution:
    def queryString(self, s: str, n: int) -> bool:
        def getBinary(num):
            res = []
            while num:
                res.append(str(num%2))
                num //= 2
            return ''.join(res[::-1])
        for i in range(1, n+1):
            if getBinary(i) not in s: return 0
        return 1