class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        # def check(num):
        #     if num not in visit: return True
        #     return False
        Q, visit = [(0, x)], set({x})
        
        def check(num):
            if num not in visit: return True
            return False
        
        while Q:
            op, a = heappop(Q)
            if a == y: return op
            if check(a+1): 
                visit.add(a+1)
                heappush(Q, (op+1, a+1))
            if check(a-1):
                visit.add(a-1)
                heappush(Q, (op+1, a-1))
            if a % 11 == 0 and check(a//11):
                visit.add(a // 11)
                heappush(Q, (op+1, a // 11))
            if a % 5 == 0 and check(a // 5):
                visit.add(a // 5)
                heappush(Q, (op+1, a // 5))