from sortedcontainers import SortedList
class RandomizedSet:

    def __init__(self):
        self.hashT = set()
        self.A = SortedList()

    def insert(self, val: int) -> bool:
        if val in self.hashT:
            return False
        self.A.add(val)
        self.hashT.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.hashT:
            self.hashT.discard(val)
            self.A.discard(val)
            return True
        return False

    def getRandom(self) -> int:
        return self.A[random.randint(0, len(self.A)-1)]