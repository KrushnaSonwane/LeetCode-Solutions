class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        
        def getList(num):
            if num == 1: return [1]
            res, curr = [1, num], num
            while num*curr <= bound:
                res.append(num*curr)
                num *= curr
            return res
        
        A = getList(x)
        B = getList(y)
        ans = set()
        
        for a in A:
            for b in B:
                if a+b <= bound:
                    ans.add(a+b)
                else:
                    break
        return [val for val in ans]