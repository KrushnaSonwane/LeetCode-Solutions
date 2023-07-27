class Solution:
    def maxRunTime(self, n: int, B: List[int]) -> int:
        B.sort()
        
        def check(x):
            sum_, count = 0, 0
            for num in B:
                sum_ += num
                if sum_ >= x:
                    sum_ -= x
                    count += 1
            return count >= n
        
        l, r = 1, sum(B)+1
        
        while r > l:
            x = (r+l)//2
            if check(x): l = x + 1
            else: r = x
                
        return l-1