class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD, hashT, res = 10**9+7, Counter(arr), 1
        arr.sort()
        for i in range(1, len(arr)):
            for j in range(i):
                a, b = arr[i], arr[j]
                if a % b == 0:
                    hashT[a] += (hashT[b] * hashT[a // b])
            res = (res + hashT[arr[i]]) % MOD
        return res