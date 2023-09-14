class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        hashT, sum_ = set(), 1
        
        for i in range(len(s)-(k-1)):
            hashT.add(s[i:i+k])
            
        for _ in range(k): sum_ *= 2
            
        return len(hashT) == sum_