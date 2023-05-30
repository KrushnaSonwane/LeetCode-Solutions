class MyHashSet:

    def __init__(self):
        self.hashT = {}

    def add(self, key: int) -> None:
        self.hashT[key] = 0

    def remove(self, key: int) -> None:
        if key in self.hashT: del self.hashT[key]

    def contains(self, key: int) -> bool:
        return key in self.hashT


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)