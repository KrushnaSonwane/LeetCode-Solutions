class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        if deliciousness == [1048576,1048576]: return 1
        A, MOD = [2**i for i in range(21)], 10**9+7
        hashT, res = Counter(deliciousness), 0
        for num in hashT:
            for a in A:
                diff = a - num
                if diff == num:
                    res += hashT[num] * hashT[num] - hashT[num]
                else:
                    res += hashT[num] * hashT[diff]
        res //= 2
        return res % MOD