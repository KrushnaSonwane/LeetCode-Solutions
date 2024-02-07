class MovingAverage:

    def __init__(self, size: int):
        self.A, self.n = [], size
        self.sum_ = 0

    def next(self, val: int) -> float:
        if len(self.A) == self.n:
            self.sum_ -= self.A.pop(0)
        self.A.append(val)
        self.sum_ += val
        return self.sum_ / float(len(self.A))


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)