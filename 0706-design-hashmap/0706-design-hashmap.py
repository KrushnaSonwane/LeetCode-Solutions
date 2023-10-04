class MyHashMap:

    def __init__(self):
        self.A = {}

    def put(self, key: int, value: int) -> None:
        self.A[key] = value

    def get(self, key: int) -> int:
        return -1 if key not in self.A else self.A[key]

    def remove(self, key: int) -> None:
        if key in self.A: del self.A[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)