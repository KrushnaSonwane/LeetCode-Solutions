from sortedcontainers import SortedList

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.A = SortedList()
        for i in range(maxNumbers):
            self.A.add(i)
        self.hashT = set()

    def get(self) -> int:
        print(self.A)
        if self.A:
            num = self.A.pop(0)
            self.hashT.add(num)
            return num
        return -1

    def check(self, number: int) -> bool:
        return number not in self.hashT

    def release(self, number: int) -> None:
        if number in self.hashT:
            self.A.add(number)
            self.hashT.discard(number)



# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)