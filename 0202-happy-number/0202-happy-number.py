class Solution:
    def isHappy(self, n: int) -> bool:
        visit = {n}
        while n != 1:
            sum_ = 0
            while n:
                sum_ += (n%10)**2
                n //= 10
            if sum_ in visit: return False
            visit.add(sum_)
            n = sum_
        return True