from sortedcontainers import SortedList
class TwoSum:

    def __init__(self):
        self.A = SortedList()

    def add(self, number: int) -> None:
        self.A.add(number)

    def find(self, value: int) -> bool:
        hashT, sum_ = Counter(self.A), 0
        for num in self.A:
            key = value-num
            if key == num and hashT[num] >= 2: return True
            elif key != num and hashT[num] >= 1 and hashT[key] >= 1: return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)