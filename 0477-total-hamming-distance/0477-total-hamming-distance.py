class Solution:
    def totalHammingDistance(self, A: List[int]) -> int:
        hashT = defaultdict(int)
        for num in A:
            curr, count = num, 0
            while curr:
                hashT[(count, curr%2)] += 1
                curr //= 2
                count += 1
        res = 0
        for val in hashT:
            c, d = val
            if d:
                res += hashT[val] * (len(A)-hashT[val])
        return res