class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        hashT = set({0})
        for li in mat:
            newHashT = set() 
            for num in li:
                for val in hashT:
                    newHashT.add(val+num)
            hashT = newHashT
        return min(abs(target-num) for num in hashT)