class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
        res = 0
        def dfs(num):
            if num < 2: return num
            return dfs(num//2) + num%2
        return sum(1 for num in range(left, right+1) if dfs(num) in primes)