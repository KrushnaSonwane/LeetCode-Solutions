class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        
        #finding the longest prefix of s2 in the suffix of s1
        def mergeString(s1, s2):
            if s2 in s1: return ''
            for i in range(len(s2)-1, -1, -1):
                p1, p2 = i, len(s1)-1
                while p2 >= 0 and p1 >= 0 and s1[p2]==s2[p1]:
                    p2 -= 1
                    p1 -= 1
                if p1 == -1: return s2[i+1:]
            return s2
        
        def f(A, B, C):
            res = A
            res += mergeString(res, B)
            res += mergeString(res, C)
            return res
        
        finalAns = "a" * 301
        
        #trying all the possibilities
        for ans in [f(a,b,c), f(a,c,b), f(b,a,c), f(b,c,a), f(c,a,b), f(c,b,a)]:
            if len(finalAns) > len(ans): #if the length of final answer is greather than the length current ans.
                finalAns = ans
            elif len(finalAns)==len(ans): #if length of both strings are same then update finalAnswer with minimun string. 
                finalAns = min(finalAns, ans)
        return finalAns
        