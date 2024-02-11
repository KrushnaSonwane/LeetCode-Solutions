from sortedcontainers import SortedList
class HitCounter:

    def __init__(self):
        self.A = SortedList()

    def hit(self, timestamp: int) -> None:
        self.A.add(timestamp)

    def getHits(self, timestamp: int) -> int:
        l, r, a = 0, len(self.A)-1, len(self.A)
        while r >= l:
            mid = (r + l) // 2
            if self.A[mid] > timestamp - 300:
                a = mid
                r = mid - 1
            else:
                l = mid + 1
        l, r, b = 0, len(self.A)-1, len(self.A)
        while r >= l:
            mid = (r + l) // 2
            if self.A[mid] < timestamp:
                r = mid - 1
            else:
                b = mid
                l = mid + 1
        return b - a
        
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)