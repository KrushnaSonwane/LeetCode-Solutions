class Logger:

    def __init__(self):
        self.A = Counter()

    def shouldPrintMessage(self, t: int, s: str) -> bool:
        if self.A[s] > t: return False
        self.A[s] = t + 10
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)