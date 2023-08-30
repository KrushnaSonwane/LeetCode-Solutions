class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        def getList(num):
            if num == 1: return [1]
            res = [1, num]
            curr = num
            while num*curr <= bound:
                res.append(num*curr)
                num *= curr
            return res
        A = getList(x)
        B = getList(y)
        ans = set()
        for num in A:
            for num2 in B:
                if num+num2 <= bound:
                    ans.add(num+num2)
        return [val for val in ans]