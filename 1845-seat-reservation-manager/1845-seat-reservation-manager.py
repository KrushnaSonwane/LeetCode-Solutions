class SeatManager:

    def __init__(self, n: int):
        self.Q = []
        for i in range(1, n+1):
            heappush(self.Q, i)

    def reserve(self) -> int:
        return heappop(self.Q)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.Q, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)