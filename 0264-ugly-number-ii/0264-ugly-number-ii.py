class Solution:
    def nthUglyNumber(self, n: int) -> int:
        Q, visit = [1], set()
        for _ in range(n-1):   
            num = heappop(Q)
            for currNum in [num*2, num*3, num*5]:
                if currNum not in visit:
                    visit.add(currNum)
                    heappush(Q, currNum)
        return heappop(Q)