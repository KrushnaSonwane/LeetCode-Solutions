class Solution:
    def singleNumber(self, A: List[int]) -> int:
        count = collections.Counter(A)
        for num in count: 
            if count[num] == 1: return num