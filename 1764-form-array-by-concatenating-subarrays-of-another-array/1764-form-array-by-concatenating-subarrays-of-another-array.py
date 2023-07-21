class Solution:
    def canChoose(self, G: List[List[int]], A: List[int]) -> bool:
        S = ''.join("."+str(num)+"." for num in A)
        for B in G:
            newS = ''.join("."+str(num)+'.' for num in B)
            if newS not in S: return 0
            S = S[S.index(newS)+len(newS): ]
        return 1