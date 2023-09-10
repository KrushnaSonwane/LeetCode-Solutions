class Solution:
    def countOrders(self, n: int) -> int:
        mod, res = 10**9+7, 1
        for i in range(1, n+1):
            res = (res * (i*2-1) * i) % mod
        return res