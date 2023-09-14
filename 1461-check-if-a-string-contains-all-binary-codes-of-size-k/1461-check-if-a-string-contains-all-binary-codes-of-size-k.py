class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        hashT = set()
        for i in range(len(s)-(k-1)):
            hashT.add(s[i:i+k])
        sum_ = 1
        for _ in range(k):
            sum_ *= 2
        return len(hashT) == sum_