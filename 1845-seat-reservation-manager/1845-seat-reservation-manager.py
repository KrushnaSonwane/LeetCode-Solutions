class SeatManager:

    def __init__(self, n: int):
        self.queue = [i for i in range(1, n + 1)]
        heapq.heapify(self.queue)

    def reserve(self) -> int:
        return heapq.heappop(self.queue)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.queue, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)